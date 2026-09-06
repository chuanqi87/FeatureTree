# Configure internationalization (i18n) rewrites

Use internationalization rewrites ("i18n rewrites") to serve different content
depending on a user's country or preferred language. Here are some example
configurations that you could set up:

* **Serve the same French content to *all* users who prefer French (regardless
  of country).**  
  Example: a homepage with French text
* **Serve Standard French content to users who prefer French, but for
  *Canadian* users who prefer French, serve Canadian French content
  instead.**  
  Example: a homepage with Standard French phrasing versus a homepage with
  Canadian French phrasing
* **Serve the same content to *all* Canadian users (regardless of their
  language preference).**  
  Example: a homepage with your site's "default" language but with a
  Canada-specific feature (like a holiday theme)
* **Serve Canadian French content to Canadian users who prefer French.**  
  Example: a homepage with Canadian French phrasing and a Canada-specific
  feature (like a holiday theme)

Firebase Hosting determines a user's country from their IP address and a
user's language preferences from the `Accept-Language` request header (usually
[set automatically by their web browser](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language#wikiArticle)).

## Set up i18n rewrites

To set up i18n rewrites for your Hosting site, you need to create an "i18n
content" directory for all your localized content, then add the `i18n` attribute
to your `firebase.json` file to point to your new "i18n content" directory.

Here are the detailed steps:

1. Within your local app directory's `public` folder, make a separate directory
   for your "i18n content", then create subfolders for each language and
   country combination supported by your site.

   In each subfolder, add the content specific for that combination, like
   holiday-themed homepages or language-specific 404 pages.

   Here's an example "i18n content" directory called `localized-files`:

   ```
   public/
       index.html  // your site's default homepage
       404.html  // your site's custom 404 page

       localized-files/
           ALL_ca/
               index.html
           es_ALL/
               index.html
               404.html
           fr/
               index.html
               404.html
           fr_ca/
               index.html
   ```

   **View the matching requests for each subfolder's content**

   ```
   public/
       // matches requests that aren't specified by your "i18n content" subfolders
       // example: display your homepage in the "default" language for your site with no country-specific features
       index.html  // your site's default homepage
       404.html  // your site's custom 404 page

       localized-files/

           // matches requests from Canada with any language preference
           // example: display your homepage in the "default" language for your site with a Canada-specific feature
           ALL_ca/
               index.html

           // matches requests from any country with a language preference of `es` or `es-foo`
           // example: display your homepage in Spanish with no country-specific features
           es_ALL/
               index.html
               404.html  // your site's custom 404 page in Spanish

           // matches requests from any country with a language preference of `fr` or `fr-foo`
           // example: display your homepage in Standard French with no country-specific features
           fr/
               index.html
               404.html  // your site's custom 404 page in French

           // matches requests from Canada with a language preference of `fr` or `fr-foo`
           // example: display your homepage in Canadian French and/or with a Canada-specific feature
           fr_ca/
               index.html
   ```

   The `localized-files/` directory contains separate subfolders for each
   language and country combination supported by your site. The naming pattern
   for each subfolder must follow either of these formats:

   * **`languageCode_countryCode`**: Contains content specific for users
     who have that language preference *and* that country code
   * **`languageCode`**: Contains content specific for users who have that
     language preference, but the content isn't country-specific; basically
     equivalent to `languageCode_ALL`

   Refer to the subsection
   [Country and language codes](https://firebase.google.com/docs/hosting/i18n-rewrites#country-and-language-codes) below
   for more details about these codes. You can use the value of `ALL`
   (case-sensitive) to indicate *any* country (like `es_ALL/`) or *any*
   language (like `ALL_ca/`).

   The files in a subfolder don't need to have analogous files in the `public`
   directory or other subfolders. You can create content that is entirely
   specific to a language and/or country.

   **Note:** Review
   [Priority order for "i18n content"](https://firebase.google.com/docs/hosting/i18n-rewrites#priority-order) below
   to learn the order in which Hosting serves your "i18n content" files.
2. Add the `i18n` attribute to your `firebase.json` file and specify the
   directory that contains your "i18n content". Continuing our example:

   ```
   // firebase.json

   "hosting": {

     "public": "public",

     "ignore": [
       "firebase.json",
       "**/.*",
       "**/node_modules/**"
     ],

     "i18n": {
       "root": "/localized-files"  // directory that contains your "i18n content"
     }

     ...
   }
   ```

   The directory specified for `root` must be the name of the directory that
   contains all your "i18n content" subfolders. If you placed all your
   "i18n content" subfolders at the root of your `public` directory, use `/`
   for the value of `root`. Leading and trailing slashes in the `root` value
   are optional.
3. Deploy your "i18n content" and config to your Hosting site.

You can test your setup using [cookie overrides](https://firebase.google.com/docs/hosting/i18n-rewrites#cookie-overrides).

### Country and language codes

When naming "i18n content" subfolders, you must use lowercase for both country
and language codes. You can use the value of `ALL` (case-sensitive) to indicate
*any* country (like `es_ALL/`) or *any* language (like `ALL_ca/`).

Hosting obtains the country code from the user's IP address. Country codes
are two-letter
[ISO 3166-1 alpha-2 codes](https://en.wikipedia.org/wiki/ISO_3166-1).

The language codes are obtained from the user's `Accept-Language` request header
(usually
[set automatically by their web browser](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language#wikiArticle)).
They are [ISO 639-1 codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
Keep the following in mind when using language codes:

* When Hosting searches for which "i18n content" to serve, it orders the
  languages based on the quality values in the `Accept-Language` header.
* Hosting drops any regional and country subtags in the `Accept-Language`
  header, so the language code in a "i18n content" subfolder name cannot
  contain these subtags. For example, you can't use `es-419` or `es-US` as a
  language code in a subfolder name, but you can use `es`.

  If you want to serve specific regional or country content, you can create
  subfolders that contain the specific language-country content you want to
  support.

  View examples to support specific regional or country content

  **Serve Spanish content applicable for Spain versus
  *any* other country (mimic the behavior of `es-419`)**

  In this example, a request from Spain with the language preference of
  `es`, `es-es`, or even `es-419` would receive content from the `es_es/`
  subfolder because Hosting treats all those language codes as `es`.

  A request from the United States, Mexico, or any other country with the
  language preference of `es-419` would receive content from the `es_ALL/`
  subfolder because Hosting treats `es-419` as `es`.

  ```
  public/
      // matches requests that aren't specified by your "i18n content" subfolders
      index.html  // the site's default homepage

      localized-files/

          // matches requests from Spain with a language preference of `es` or `es-foo`
          es_es/
              index.html

          // matches requests from any other country with a language preference of `es` or `es-foo`
          es_ALL/
              index.html
  ```

  **Serve Spanish content applicable for
  *specific* countries**

  In this example, a request from Mexico with the language preference of
  `es-419` would receive content from the `es_mx/` subfolder because
  Hosting treats the language code `es-419` as `es`.

  However, a request from the United States with the language preference of
  `es-419` would receive content from the `es_ALL/` subfolder because
  Hosting treats `es-419` as `es` *and* there's no `es_us/` subfolder.

  ```
  public/
      // matches requests that aren't specified by your "i18n content" subfolders
      index.html  // the site's default homepage

      localized-files/

          // matches requests from Argentina with a language preference of `es` or `es-foo` (mimics behavior of `es-ar` header tag)
          es_ar/
              index.html

          // matches requests from Spain with a language preference of `es` or `es-foo` (mimics behavior of `es-es` header tag)
          es_es/
              index.html

          // matches requests from Mexico with a language preference of `es` or `es-foo` (mimics behavior of `es-mx` header tag)
          es_mx/
              index.html

          // matches requests from any other country with a language preference of `es` or `es-foo` (mimics behavior of `es-419` header tag)
          es_ALL/
              index.html
  ```

## Priority order for "i18n content"

If you set up i18n rewrites, Hosting serves content based on the following
priority order:

1. Reserved namespaces that begin with a `/__/*` path segment
2. Configured [redirects](https://firebase.google.com/docs/hosting/full-config#redirects)
3. Exact-match static content

   1. Language code + Country code (for example, content from `fr_ca/`)  
      The order follows the quality values for each language in the request's
      `Accept-Language` header.
   2. Country code only (for example, content from `ALL_ca/`)
   3. Language code only (for example, content from `fr/` or `es_ALL/`)  
      The order follows the quality values for each language in the request's
      `Accept-Language` header.
   4. "Default" exact-match static content  
      This is content that's outside the "i18n content" directory, like at the
      root of the `public` directory.
4. Configured [rewrites](https://firebase.google.com/docs/hosting/full-config#rewrites)
5. 404 handling

   1. i18n 404 pages  
      This follows the same priority order listed above for exact-match
      static content.
   2. [Custom 404](https://firebase.google.com/docs/hosting/full-config#404) page
   3. Default 404 page (provided by Firebase)

### Example for priority order

Let's continue our example from above. We'll use the same example directory and
an example request.

* **Example local project directory with an "i18n content" directory (called `localized-files`)**

  ```
  public/
      index.html  // your site's default homepage
      404.html  // your site's custom 404 page

      localized-files/
          ALL_ca/
              index.html
          es_ALL/
              index.html
              404.html
          fr/
              index.html
              404.html
          fr_ca/
              index.html
  ```
* **Example request information**

  + Language codes: `fr`, `en` (French, then English)  
    The language codes are ordered based on quality values in the
    `Accept-Language` header.
  + Country code: `ca` (Canada)

According to the exact-match priority order and the quality values for the
language preferences, Hosting will search the directories for a requested
page in the following order.

1. `public/localized-files/fr_ca/`
2. `public/localized-files/en_ca/`
3. `public/localized-files/ALL_ca/`
4. `public/localized-files/fr_ALL/`
5. `public/localized-files/fr/`
6. `public/localized-files/en_ALL/`
7. `public/localized-files/en/`
8. `public/`
9. 404 handling

**Which page will be served to the user?**

* Requested page: `index.html`

  Answer

  > `index.html` from the `fr_ca/` subfolder
  >
  > Since Hosting searches the `fr_ca/` subfolder first, it will find the
  > exact-match for `index.html` in that subfolder.
* Requested page: `awesome-page.html`

  Answer

  > `404.html` from the `fr/` subfolder
  >
  > Hosting first searches the entire directory (including all the
  > "i18n content" subfolders and root directory) in priority order for an
  > exact-match, but there's not an exact-match for `awesome-page.html`.
  >
  > So, Hosting will start its 404 handling, which follows the same i18n
  > priority order as exact-match searches. The `fr/` subfolder is the first
  > subfolder searched that contains a 404 page.

Note the following about this search-and-serve of the "i18n content" directory:

* The `localized-files/` directory doesn't actually contain `en_ca/`,
  `en_ALL/`, or `en/` subfolders, so Hosting will just skip down the
  priority list until it finds a matching subfolder for the request's
  language-country combination.
* Even though the `localized-files/` directory contains an `es_ALL/`
  subfolder, the example *request* above doesn't include an `es` or `es-foo`
  language code, so Hosting will not search for "i18n content" that
  matches `es`.
* Subfolders called `fr/` and `fr_ALL/` are equivalent from the perspective of
  a user's country and language preferences. However, if both subfolders
  exist, Hosting will serve `fr_ALL/` content before `fr/` content.

## Override language and country codes with cookies

You can change what content is served by using cookies to override the country
and language headers.

Here are some ways you can use cookie overrides:

* Test a feature with different language/country combinations to check which
  content is served.
* Enable your users to change the content that they see. For example, you can
  implement a language picker, then set the user's
  `firebase-language-override` cookie accordingly.

To configure cookie overrides, set cookies with both or either of these names:
`firebase-country-override` and `firebase-language-override`. For example,
the following JavaScript code snippet overrides the country code to be `ca` and
the `Accept-Language` header to be `fr,en`:

```
document.cookie = "firebase-country-override=ca";
document.cookie = "firebase-language-override=fr,en";
```

Language cookie overrides must be a comma-separated list of language codes in
order of preference, without subtags or quality values.

Cookie overrides are not reflected in logs.
