import logging

from webcrawler import (domain_filters, duplicate_detector, html_fetcher,
                        html_parser, page_repository, url_filter, url_frontier)
from webcrawler.page import Page


SEED_URLS_FILE_PATH = 'data/seed_urls.txt'
DOMAIN_FILTERS_FILE_PATH = 'data/domain_filters.txt'

LOG_FILE_PATH = 'data/log.txt'
LOG_LEVEL = logging.INFO


logging.basicConfig(level=LOG_LEVEL, filename=LOG_FILE_PATH, filemode='w')


def crawl():
    while page_repository.have_capacity() and not url_frontier.empty():
        url = url_frontier.pop()
        page = Page(url)

        # fetch html
        html_content = html_fetcher.fetch(page)
        if html_content is None:
            continue

        page.html = html_content

        # parse html
        parsed_content = html_parser.parse(page)
        if parsed_content is None:
            continue

        page.parsed_content = parsed_content

        # check for duplication
        if duplicate_detector.have_duplicate_content(page):
            continue

        # save page to page repository
        page_repository.save_page(page)

        # extract and filter links
        links = url_filter.filter_urls(html_parser.extract_links(page))

        # add links to the frontier
        for link in links:
            if not duplicate_detector.is_duplicate_url(link):
                url_frontier.add(link)

    print(f'Crawled {page_repository.page_count} pages.')


def run():
    url_frontier.initialize(SEED_URLS_FILE_PATH)
    domain_filters.initialize(DOMAIN_FILTERS_FILE_PATH)

    page_repository.start()

    crawl()

    page_repository.finish()
