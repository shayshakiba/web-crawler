"""Fetcher for HTML pages."""


import logging
import requests


logger = logging.getLogger('fetcher')


def fetch(url: str) -> str | None:
    """Fetch the page content.

    Args:
        url (str): The given URL.

    Returns:
        str | None: The HTML content.
            None if the content-type isn't 'text/html' or the request is unsuccessful.
    """
    if not _check_content_type(url):
        return None

    try:
        response = requests.get(url, allow_redirects=True)
    except Exception:
        logger.error(f"'{url}' can't be fetched.")

        return None

    return response.text


def _check_content_type(url: str) -> bool:
    """Check the content type.

    Args:
        url (str): The given URL.

    Returns:
        bool: True if the content type is 'text/html'.
    """
    try:
        response = requests.head(url, allow_redirects=True)
        content_type = response.headers['content-type']
    except Exception:
        logger.error(f"'{url}' header can't be fetched.")

        return False

    # whether the content type is 'text/html' or not
    return 'text/html' in content_type
