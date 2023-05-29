from dataclasses import dataclass

from html_parser import ParsedContent


@dataclass
class Page:
    url: str
    html: str | None = None
    parsed_content: ParsedContent | None = None
