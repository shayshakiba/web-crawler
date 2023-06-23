from dataclasses import dataclass
from typing import NamedTuple


ParsedContent = NamedTuple('ParsedContent', [('title', str), ('body', str)])


@dataclass
class Page:
    url: str
    html: str | None = None
    parsed_content: ParsedContent | None = None
