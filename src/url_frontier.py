"""A component for handling URLs eligible to be crawled.

This module stores the URLs in a FIFO queue, resulting in a breadth-frist traversal.
"""


from collections import deque


_url_frontier: deque[str] = deque()


def empty() -> bool:
    return len(_url_frontier) == 0


def add(url: str) -> None:
    _url_frontier.appendleft(url)


def pop() -> str:
    return _url_frontier.pop()
