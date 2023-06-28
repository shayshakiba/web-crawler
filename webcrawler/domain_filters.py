"""A component for storing domain filters.

This module acts as a singleton resource.
"""


_domain_filters: set[str] = set()


def initialize(file_path: str) -> None:
    with open(file_path, 'r') as input_file:
        for line in input_file:
            domain = line.strip()
            _domain_filters.add(domain)


def empty() -> bool:
    return len(_domain_filters) == 0


def add(domain: str) -> None:
    _domain_filters.add(domain)


def contains(domain: str) -> bool:
    return domain in _domain_filters
