"""Render Apple's structured document response when a Markdown representation is absent."""

import json

from .urls import canonical


def render(raw, url):
    data=json.loads(raw)
    metadata=data.get('metadata',{})
    if not isinstance(metadata,dict) or not metadata.get('title'):
        raise ValueError('DocC response has no document title')
    references=data.get('references',{})
    unknown=set()

    def reference(identifier):
        ref=references.get(identifier,{})
        title=ref.get('title',identifier)
        target=ref.get('url')
        return f'[{title}]({target})' if target else title

    def node(value):
        if isinstance(value,str):
            return value
        if isinstance(value,list):
            return ''.join(node(item) for item in value)
        if not isinstance(value,dict):
            return ''
        tag=value.get('type',value.get('kind',''))
        if tag=='text':return value.get('text','')
        if tag=='codeVoice':return '`'+value.get('code','')+'`'
        if tag=='reference':return reference(value.get('identifier',''))
        if tag=='heading':return '\n'+'#'*min(6,value.get('level',2))+' '+value.get('text','')+'\n\n'
        if tag=='paragraph':return node(value.get('inlineContent',[]))+'\n\n'
        if tag in ('emphasis','strong','strikethrough'):
            marker={'emphasis':'*','strong':'**','strikethrough':'~~'}[tag]
            return marker+node(value.get('inlineContent',[]))+marker
        if tag in ('superscript','subscript'):
            marker = 'sup' if tag == 'superscript' else 'sub'
            return '<'+marker+'>'+node(value.get('inlineContent',[]))+'</'+marker+'>'
        if tag=='technologies':
            groups=[]
            for group in value.get('groups',[]):
                groups.append('## '+group.get('name','Technologies')+'\n\n')
                for technology in group.get('technologies',[]):
                    groups.append('- '+node(technology.get('destination',{}))+'\n')
                    groups.append(node(technology.get('content',[])))
            return ''.join(groups)+'\n'
        if tag=='codeListing':return '\n```'+value.get('syntax','')+'\n'+'\n'.join(value.get('code',[]))+'\n```\n\n'
        if tag in ('unorderedList','orderedList'):
            return ''.join(f"{str(i+1)+'.' if tag=='orderedList' else '-'} "+node(item.get('content',[])).strip()+'\n'
                           for i,item in enumerate(value.get('items',[])))+'\n'
        if tag=='aside':
            return '\n> '+value.get('name',value.get('style','Note'))+'\n'+''.join(
                '> '+line+'\n' for line in node(value.get('content',[])).splitlines())+'\n'
        if tag=='table':
            rows=value.get('rows',[]);lines=[]
            for i,row in enumerate(rows):
                cells=row if isinstance(row,list) else row.get('cells',[])
                rendered=[node(cell).strip().replace('\n','<br>').replace('|','\\|') for cell in cells]
                lines.append('| '+' | '.join(rendered)+' |')
                if i==0:lines.append('| '+' | '.join(['---']*len(rendered))+' |')
            return '\n'.join(lines)+'\n\n'
        if tag in ('image','video'):
            ref=references.get(value.get('identifier'),{})
            return '[Media: '+str(ref.get('alt',value.get('identifier','')))+']\n'
        if tag=='termList':
            return ''.join('**'+node(item.get('term',{}))+'**\n'+node(item.get('definition',{}))
                           for item in value.get('items',[]))
        if tag not in ('','content','text','declarations','parameters','discussion','topics','relationships'):
            unknown.add(tag)
        return ''.join(node(value[key]) for key in ('inlineContent','content','items','sections') if key in value)

    parts=['# '+metadata['title']+'\n\n',node(data.get('abstract',[]))+'\n\n']
    for section in data.get('primaryContentSections',[]):
        if section.get('kind')=='declarations':
            for declaration in section.get('declarations',[]):
                tokens=''.join(t.get('text','') for t in declaration.get('tokens',[]))
                parts.append('```\n'+tokens+'\n```\n\n')
        elif section.get('kind')=='parameters':
            parts.append('## Parameters\n\n')
            for param in section.get('parameters',[]):
                parts.append('### '+param.get('name','')+'\n\n'+node(param.get('content',[])))
        else:parts.append(node(section))
    parts.append(node(data.get('sections',[])))
    for section in data.get('topicSections',[])+data.get('seeAlsoSections',[]):
        parts.append('## '+section.get('title','Topics')+'\n\n')
        parts.extend('- '+reference(identifier)+'\n' for identifier in section.get('identifiers',[]))
    links=[]
    for ref in references.values():
        target=canonical(ref.get('url',''),url)
        if ref.get('type')=='topic' and target:
            links.append(target)
    meta={**metadata,'source_format':'docc-json','availability':metadata.get('platforms',[]),
          'unhandled_render_types':sorted(unknown)}
    return metadata['title'],''.join(parts),sorted(set(links)),meta
