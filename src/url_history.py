"""A component for storing discovered URLs."""


_url_history: set[str] = set()


def add(url: str) -> None:
    _url_history.add(url)


def contains(url: str) -> bool:
    return url in _url_history
