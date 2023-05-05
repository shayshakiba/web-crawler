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

        # extract and process links
        links = html_parser.extract_links(url, html_content)

        for link in links:
            # check url duplication
            if duplicate_detector.is_duplicate_url(link):
                continue

            # save url to history
            duplicate_detector.save_url(link)

            # add to frontier
            url_frontier.add(link)


if __name__ == '__main__':
    initiate_url_frontier()

    crawl()
