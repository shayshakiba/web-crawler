"""Handling history and duplicate detection for URLs and content."""


import content_history
import url_history
from page import Page


def is_duplicate_url(url: str) -> bool:
    """Check if the same URL has been discovered before.

    If the URL isn't a duplicate, it will be added to the URL history as a side effect.

    Args:
        url (str): The URL.

    Returns:
        bool: True if the URL is a duplicate.
    """
    if not url_history.contains(url):
        url_history.add(url)

        return False

    return True


def have_duplicate_content(page: Page) -> bool:
    """Check if the same content has been discovered before.

    If the content isn't a duplicate, it will be added to the content history as a side effect.

    Args:
        page (Page): The page.
            It should contain an initialized parsed content.

    Returns:
        bool: True if the content is a duplicate.
    """
    if not content_history.contains(page.parsed_content.body):
        content_history.add(page.parsed_content.body)

        return False

    return True
