"""Parser for HTML pages."""


import logging
from typing import NamedTuple
from bs4 import BeautifulSoup


logger = logging.getLogger('parser')


ParsedContent = NamedTuple('ParsedContent', [('title', str), ('body', str)])


def parse(html_content: str) -> ParsedContent:
    soup = BeautifulSoup(html_content, 'html.parser')

    title = soup.title.decode_contents()
    body = soup.body.decode_contents()

    return ParsedContent(title, body)
