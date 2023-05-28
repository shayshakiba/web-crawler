from dataclasses import dataclass

from html_parser import ParsedContent


@dataclass
class Page:
    url: str
    html: str
    parsed_content: ParsedContent
