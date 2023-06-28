from dataclasses import dataclass
from typing import NamedTuple


class ParsedContent(NamedTuple):
    title: str
    body: str


@dataclass
class Page:
    url: str
    html: str | None = None
    parsed_content: ParsedContent | None = None
 