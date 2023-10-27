####Problem
-------
Write an HTTP API for url shortener service(https://en.wikipedia.org/wiki/URL_shortening) with three components.

- Create API should take a long url and return a short url. API doesn't require authentication.

- API should have an endpoint for search. Search will return results matching the title of the url.
Say term "Python", api should return all pages which have partial or full match for the term
with the title of the page and url.

Web interface for URL shortener

Good to have

- Url shortener service should store metadata about short url like total number of hits.
An API with shortened url should return the data.

Note: Use Python flask and don't use any API framework. Please feel free to ask any question
