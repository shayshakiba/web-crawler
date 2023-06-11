# Web Crawler

A single-threaded web crawler for HTML web pages.

<img width="3207" alt="Web Crawler Structure" src="https://github.com/shayshakiba/web-crawler/assets/70333359/32bfb122-f476-4f56-b8ba-0239b121fd3b">

## Usage

First, install the required modules: `pip install -r requirements.txt`

Then, set the seed URLs, domain filters, and page limit:
  * The crawling process will be started with the seed URLs, therefore, at least one seed URL is required. Each line in `data/seed_urls.txt` have to a be fully qualified URL (e.g. `https://docs.python.org`).
  * Domain filters can optionally be specified to limit the crawling to a certain group of domains. Each line in `data/domain_filters.txt` have to be a domain name (e.g. `docs.python.org` or `python.org`).
  * The number of pages to be crawled can be specified by configuring `PAGE_LIMIT` located in `src/page_repository.py`.

Finally, run the program: `python src/main.py`
