"""Parser for HTML pages."""


import logging
from typing import NamedTuple
from bs4 import BeautifulSoup
from urllib.parse import urljoin


logger = logging.getLogger('parser')


ParsedContent = NamedTuple('ParsedContent', [('title', str), ('body', str)])


def parse(html_content: str) -> ParsedContent | None:
    soup = BeautifulSoup(html_content, 'html.parser')

    title = soup.title
    body = soup.body

    if title is None or body is None:
        return None

    return ParsedContent(title.decode_contents(), body.decode_contents())


def extract_links(base_url: str, html_content: str) -> list[str] | None:
    soup = BeautifulSoup(html_content, 'html.parser')

    links = [node.get('href') for node in soup.find_all('a')]

    if len(links) == 0:
        return None

    return _normalize_links(base_url, links)


def _normalize_links(base_url: str, links: list[str]) -> list[str]:
    return [urljoin(base_url, link) for link in links]
