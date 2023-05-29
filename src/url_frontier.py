"""A component for handling URLs eligible to be crawled.

This module acts as a singleton resource which stores the uncrawled URLs.
The URLs are stored in a FIFO queue, resulting in a breadth-first traversal.
"""


from collections import deque


_url_frontier: deque[str] = deque()


def initialize(file_path: str) -> None:
    with open(file_path, 'r') as input_file:
        for line in input_file:
            url = line.strip()
            add(url)


def empty() -> bool:
    return len(_url_frontier) == 0


def add(url: str) -> None:
    _url_frontier.appendleft(url)


def pop() -> str:
    return _url_frontier.pop()
