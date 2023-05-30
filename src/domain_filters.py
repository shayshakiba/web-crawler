"""A component for storing domain filters.

This module acts as a singleton resource.
"""


_domain_filters: set[str] = set()


def initialize(file_path: str) -> None:
    global _no_domain_filter

    with open(file_path, 'r') as input_file:
        for line in input_file:
            domain = line.strip()
            _domain_filters.add(domain)

    if len(_domain_filters) == 0:
        _no_domain_filter = True


def empty() -> bool:
    return len(_domain_filters) == 0


def add(domain: str) -> None:
    _domain_filters.add(domain)


def contains(domain: str) -> bool:
    return domain in _domain_filters
