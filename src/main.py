import logging

import domain_filters
import duplicate_detector
import html_fetcher
import html_parser
import page_repository
import url_filter
import url_frontier
from page import Page


SEED_URLS_FILE_PATH = 'data/seed_urls.txt'
DOMAIN_FILTERS_FILE_PATH = 'data/domain_filters.txt'

LOG_FILE_PATH = 'out/log.txt'
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


if __name__ == '__main__':
    url_frontier.initialize(SEED_URLS_FILE_PATH)
    domain_filters.initialize(DOMAIN_FILTERS_FILE_PATH)

    page_repository.start()

    crawl()

    page_repository.finish()
