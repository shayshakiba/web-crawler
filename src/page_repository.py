"""A component for managing the page repository."""


import logging

from page import Page


PAGE_REPOSITORY_FILE_PATH = 'data/page_repository.xml'

PAGE_LIMIT = 1000


logger = logging.getLogger('page repository')


page_count = 0


def has_capacity() -> bool:
    return page_count < PAGE_LIMIT


def start() -> None:
    _open_xml()


def save_page(page: Page) -> None:
    global page_count

    _save_page_to_xml(page)

    page_count += 1

    logger.info(f"{page_count}:'{page.url}' stored in the page repository.")


def finish() -> None:
    _close_xml()


def _open_xml() -> None:
    with open(PAGE_REPOSITORY_FILE_PATH, 'w') as output_file:
        output_file.write('<xml>\n')


def _save_page_to_xml(page: Page) -> None:
    with open(PAGE_REPOSITORY_FILE_PATH, 'a') as output_file:
        output_file.write(f'<page id={page_count + 1}>\n')

        output_file.write(f'<url>{page.url}</url>\n')

        output_file.write(f'<title>{page.parsed_content.title}</title>\n')

        output_file.write(f'<body>{page.parsed_content.body}</body>\n')

        output_file.write('</page>\n')


def _close_xml() -> None:
    with open(PAGE_REPOSITORY_FILE_PATH, 'a') as output_file:
        output_file.write('</xml>\n')
