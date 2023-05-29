from dataclasses import dataclass

from parsed_content import ParsedContent


@dataclass
class Page:
    url: str
    html: str | None = None
    parsed_content: ParsedContent | None = None
