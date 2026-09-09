"""Parse source bodies; reject HTML shells and retain source navigation metadata."""

from dataclasses import dataclass, field
import json
import re

from bs4 import BeautifulSoup
from markdownify import markdownify
from lxml import html as lxml_html

from featuretree.corpus.urls import canonical


@dataclass
class Content:
    title: str
    body: str
    links: list[str] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)
    quality: str = 'ready'


def markdown_links(text, base):
    # Balanced parentheses are common in Apple symbol URLs.
    links = []
    for match in re.finditer(r'(?<!!)\[[^\]\n]*\]\(', text):
        start = match.end(); depth = 1; end = start
        while end < len(text) and depth:
            depth += (text[end] == '(') - (text[end] == ')')
            end += 1
        if not depth:
            url = canonical(text[start:end-1].split(' "')[0], base)
            if url:
                links.append(url)
    return sorted(set(links))


def parse_markdown(raw, url):
    text = raw.decode('utf-8-sig')
    if re.match(r'\s*(?:<!doctype|<html)', text, re.I):
        raise ValueError('Expected Markdown, received HTML shell')
    metadata = {}
    header = re.match(r'\s*<!--\s*(\{.*?\})\s*-->', text, re.S)
    if header:
        metadata = json.loads(header.group(1))
    content = re.sub(r'<!--.*?-->', '', text, flags=re.S).strip()
    titles = re.findall(r'^#\s+(.+)', content, re.M)
    if not titles or 'This page requires JavaScript' in content:
        raise ValueError('No document heading or received JavaScript shell')
    if re.search(r'^#\s*(404|Page Not Found|页面不存在|文档不存在)\s*$', content, re.M | re.I):
        raise ValueError('Document is an error page')
    metadata['unresolved_media'] = len(re.findall(r'https://media:', content))
    return Content(titles[0], content + '\n', markdown_links(content, url), metadata,
                   'thin' if len(re.sub(r'\[[^\]]+\]\([^\n]*?\)', '', content)) < 100 else 'ready')


def parse_html(raw, url):
    document = lxml_html.fromstring(raw)
    articles = document.xpath('//*[contains(concat(" ", normalize-space(@class), " "), " devsite-article-body ")]')
    legacy = '/sdk/api_diff/' in url and document.xpath('//meta[@name="generator" and starts-with(@content,"JDiff")]')
    if legacy and not articles:
        title = ' '.join(document.xpath('//title/text()')).strip()
        frames = document.xpath('//frame/@src')
        if frames:
            links = sorted({link for src in frames if (link := canonical(src, url))})
            return Content(title, '# '+title+'\n\n'+''.join('- ['+link+']('+link+')\n' for link in links),
                           links, {'source_format':'jdiff-frameset'}, 'thin')
        articles = document.xpath('//body')
    if not articles:
        raise ValueError('No official article body; possible shell or access page')
    title_nodes = document.xpath('//h1') or document.xpath('//title')
    title = ' '.join(title_nodes[0].itertext()).strip() if title_nodes else url.rsplit('/', 1)[-1]
    title = ' '.join(title.split('Stay organized with collections')[0].split())
    soup = BeautifulSoup(lxml_html.tostring(articles[0],encoding='unicode'), 'lxml')
    article = soup.select_one('.devsite-article-body') or soup.body
    generated_panels = article.select('devsite-key-takeaways-panel')
    excluded_summaries = len(generated_panels)
    for panel in generated_panels:
        panel.decompose()
    links = []
    for tag in article.select('a[href]'):
        link = canonical(tag['href'], url)
        if link:
            links.append(link)
        from urllib.parse import urljoin
        tag['href'] = urljoin(url, tag['href'])
    for tag in article.select('script, style, nav, button, devsite-feedback'):
        tag.decompose()
    for tag in article.select('[id]'):
        tag.insert_before(soup.new_tag('a', id=tag['id']))
    body = '# ' + title + '\n\n' + markdownify(str(article), heading_style='ATX',
                                                  strip=['script', 'style'], wrap=False)
    metadata = {'source_format': 'jdiff-html' if legacy else 'html',
                'excluded_generated_summaries': excluded_summaries,
                'anchors': [x.get('id') for x in soup.select('[id]')]}
    return Content(title, body.strip() + '\n', sorted(set(links)), metadata,
                   'thin' if len(article.get_text(strip=True)) < 100 else 'ready')


def parse(raw, url, content_type):
    content_type = (content_type or '').lower()
    if 'json' in content_type and 'developer.apple.com/' in url:
        from featuretree.corpus.docc import render
        title,body,links,metadata=render(raw,url)
        quality='partial' if metadata['unhandled_render_types'] else 'thin' if len(body)<100 else 'ready'
        return Content(title,body,links,metadata,quality)
    if 'markdown' in content_type or raw.lstrip().startswith((b'#', b'<!--')):
        return parse_markdown(raw, url)
    if 'html' in content_type:
        return parse_html(raw, url)
    if 'text/plain' in content_type and url.split('?', 1)[0].endswith('.txt'):
        text = raw.decode('utf-8-sig')
        if not text.strip() or '\x00' in text or re.match(r'\s*<(?:!doctype|html)', text, re.I):
            raise ValueError('Empty or non-text response')
        title = url.rsplit('/', 1)[-1]
        return Content(title, '# ' + title + '\n\n```text\n' + text.rstrip() + '\n```\n',
                       metadata={'source_format': 'plain-text'},
                       quality='ready' if len(text.strip()) >= 100 else 'thin')
    raise ValueError(f'Unsupported document content type: {content_type}')
