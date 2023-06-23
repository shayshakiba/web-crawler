"""A component for storing discovered content.

This module acts as a singleton resource.
"""


from hashlib import md5


_content_history: set[str] = set()


def add(content: str) -> None:
    hashed_content = md5(content.encode()).hexdigest()

    _content_history.add(hashed_content)


def contains(content: str) -> bool:
    hashed_content = md5(content.encode()).hexdigest()

    return hashed_content in _content_history
