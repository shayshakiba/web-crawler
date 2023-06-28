"""A component for managing the page repository."""


import logging
import zlib

from webcrawler.page import Page


PAGE_REPOSITORY_FILE_PATH = 'data/page_repository.xml'

PAGE_LIMIT = 1000


logger = logging.getLogger('page repository')


page_count = 0


def have_capacity() -> bool:
    """Check if the number of crawled pages is less than the specified page limit.

    Returns:
        bool: True if the page repository have capacity.
    """
    return page_count < PAGE_LIMIT


def start() -> None:
    """Start the page repository.

    This function should be called before starting to use the page repository.
    """
    _initialize_xml()


def save_page(page: Page) -> None:
    """Save the page to the page repository.

    Args:
        page (Page): The page.
    """
    global page_count

    _save_page_to_xml(page)

    page_count += 1

    logger.info(f"{page_count}:'{page.url}' stored in the page repository.")


def finish() -> None:
    """Finish the page repository.

    This function should be called when using the page repository is finished.
    """
    _close_xml()


def _initialize_xml() -> None:
    """Initialize the XML file and insert the xml opening tag."""
    with open(PAGE_REPOSITORY_FILE_PATH, 'w') as output_file:
        output_file.write('<xml>\n')


def _save_page_to_xml(page: Page) -> None:
    """Save the page to the XML file.

    This function saves the URL, title, and body of the page.

    Args:
        page (Page): The page.
    """
    with open(PAGE_REPOSITORY_FILE_PATH, 'a') as output_file:
        output_file.write(f'<page id="{page_count + 1}">\n')

        encoded_url = page.url.encode()
        output_file.write(f'<url>{encoded_url.hex()}</url>\n')

        encoded_title = page.parsed_content.title.encode()
        output_file.write(f'<title>{encoded_title.hex()}</title>\n')

        compressed_body = zlib.compress(page.parsed_content.body.encode())
        output_file.write(f'<body>{compressed_body.hex()}</body>\n')

        output_file.write('</page>\n')


def _close_xml() -> None:
    """Insert the xml closing tag."""
    with open(PAGE_REPOSITORY_FILE_PATH, 'a') as output_file:
        output_file.write('</xml>\n')
