import logging

import duplicate_detector
import html_fetcher
import html_parser
import page_repository
import url_frontier


logging.basicConfig(level=logging.INFO)


def initiate_url_frontier():
    pass
    # TODO: implement


def crawl():
    while not url_frontier.empty():
        url = url_frontier.pop()

        # fetch html
        html = html_fetcher.fetch(url)

        if html is None:
            continue

        # TODO: parse html

        # TODO: detect content duplication

        # TODO: save content to history

        # TODO: save page to page repository

        # TODO: extract links

        # TODO: for each exctracted link: check duplication, save to history, add to frontier


if __name__ == '__main__':
    initiate_url_frontier()

    crawl()
