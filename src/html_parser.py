"""Parser for HTML pages."""


import logging
from typing import NamedTuple
from urllib.parse import urldefrag, urljoin, urlparse

from bs4 import BeautifulSoup

from page import Page


ParsedContent = NamedTuple('ParsedContent', [('title', str), ('body', str)])


logger = logging.getLogger('html parser')


def parse(page: Page) -> ParsedContent | None:
    """Parse the page.

    Args:
        page (Page): The page.
            It should contain an initialized HTML content.

    Returns:
        ParsedContent | None: The parsed content including the title and the body text.
            None if the parse isn't successful.
    """
    soup = BeautifulSoup(page.html, 'html.parser')

    title = soup.title
    body = soup.body

    if title is None or body is None:
        logger.error(f"'{page.url}' can't be parsed.")

        return None

    return ParsedContent(_remove_redundant_whitespace(title.get_text()),
                         _remove_redundant_whitespace(body.get_text()))


def _remove_redundant_whitespace(text: str) -> str:
    """Remove redundant whitespace from the text.

    Args:
        text (str): The text.

    Returns:
        str: The processed text.
    """
    return '\n'.join([' '.join(stripped.split()) for line in text.splitlines()
                      if (stripped := line.strip())])


def extract_links(page: Page) -> list[str]:
    """Extract links from the page.

    Args:
        page (Page): The page.
            It should contain an initialized URL and HTML content.

    Returns:
        list[str]: The extracted links.
    """
    soup = BeautifulSoup(page.html, 'html.parser')

    # getting non-empty href attributes and normalizing them
    links = {_normalize_link(page, href) for a in soup.find_all('a')
             if (href := a.attrs.get('href'))}

    return list(filter(_is_valid_link, links))


def _normalize_link(base_page: Page, link: str) -> str:
    """Normalize the link.

    Args:
        base_page (Page): The base page.
            It should contain an initialized URL.
        link (str): The link.

    Returns:
        str: The normalized link.
    """
    # construct an absolute URL
    normalized_link = urljoin(base_page.url, link.strip())
    # remove the fragment identifier
    normalized_link = urldefrag(normalized_link).url

    return normalized_link


def _is_valid_link(link: str) -> bool:
    """Check if the link is valid or not.

    Args:
        link (str): The link.

    Returns:
        bool: True if the link is valid.
    """
    parsed_link = urlparse(link)

    # whether the link contain a valid scheme and network location or not
    return bool(parsed_link.scheme) and bool(parsed_link.netloc)
