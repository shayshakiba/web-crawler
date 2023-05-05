import logging
import sys

import duplicate_detector
import html_fetcher
import html_parser
import page_repository
import url_frontier


logging.basicConfig(level=logging.INFO)


SEED_URLS_PATH = 'data/seed_urls.txt'


def initiate_url_frontier(seed_urls_file_path):
    with open(seed_urls_file_path, 'r') as input_file:
        for line in input_file:
            url = line.strip()

            process_url(url)


def process_url(url: str) -> None:
    # check url duplication
    if duplicate_detector.is_duplicate_url(url):
        return

    # save url to history
    duplicate_detector.save_url(url)

    # add to frontier
    url_frontier.add(url)


def crawl():
    while not url_frontier.empty():
        url = url_frontier.pop()

        # fetch html
        html_content = html_fetcher.fetch(url)

        if html_content is None:
            continue

        # parse html
        parsed_content = html_parser.parse(html_content)

        if parsed_content is None:
            continue

        # check content duplication
        if duplicate_detector.is_duplicate_content(parsed_content):
            continue

        # save content to history
        duplicate_detector.save_content(parsed_content)

        # TODO: save page to page repository

        # extract links
        links = html_parser.extract_links(url, html_content)

        # process links
        for link in links:
            process_url(link)


if __name__ == '__main__':
    initiate_url_frontier(sys.argv[1])

    crawl()
