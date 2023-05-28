"""Handling history and duplicate detection for URLs and content."""


import content_history
import url_history
from html_parser import ParsedContent


def is_duplicate_url(url: str) -> bool:
    return url_history.contains(url)


def save_url(url: str) -> None:
    url_history.add(url)


def is_duplicate_content(content: ParsedContent) -> bool:
    return content_history.contains(content.body)


def save_content(content: ParsedContent) -> None:
    content_history.add(content.body)
