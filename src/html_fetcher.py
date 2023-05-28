"""Fetcher for HTML pages."""


import logging

import requests

from page import Page


logger = logging.getLogger('html fetcher')


def fetch(page: Page) -> str | None:
    """Fetch the page content.

    Args:
        page (Page): The given page.
            It should contain an initialized URL.

    Returns:
        str | None: The HTML content.
            None if the fetch isn't successful.
    """
    if not _check_content_type(page):
        return None

    try:
        response = requests.get(page.url, allow_redirects=True)
    except Exception:
        logger.error(f"'{page.url}' can't be fetched.")

        return None

    return response.text


def _check_content_type(page: Page) -> bool:
    """Check the page content type.

    Args:
        page (Page): The given page.
            It should contain an initialized URL.

    Returns:
        bool: True if the content type is 'text/html'.
    """
    try:
        response = requests.head(page.url, allow_redirects=True)
        content_type = response.headers['content-type']
    except Exception:
        logger.error(f"'{page.url}' header can't be fetched.")

        return False

    # whether the content type is 'text/html' or not
    return 'text/html' in content_type
