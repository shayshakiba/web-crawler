"""A component for handling domain and robots.txt filters."""


from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

import tldextract


_domain_filters: set[str] = set()
_no_domain_filter = False

_robot_filters: dict[str, RobotFileParser] = dict()


def initialize_domain_filters(file_path: str) -> None:
    global _no_domain_filter

    with open(file_path, 'r') as input_file:
        for line in input_file:
            domain = line.strip()
            _domain_filters.add(domain)

    if len(_domain_filters) == 0:
        _no_domain_filter = True


def filter(urls: list[str]) -> list[str]:
    return list(filter(_check_url, urls))


def _check_url(url: str) -> bool:
    return _check_domain_filters(url) and _check_robot_filters(url)


def _check_domain_filters(url: str) -> bool:
    extracted_url = tldextract.extract(url)
    domain = '.'.join(extracted_url)
    base_domain = extracted_url.registered_domain

    if _no_domain_filter:
        return True

    return domain in _domain_filters or base_domain in _domain_filters


def _check_robot_filters(url: str) -> bool:
    domain = '.'.join(tldextract.extract(url))

    if domain not in _robot_filters:
        _robot_filters[domain] = _get_robot(url)

    robot_parser = _robot_filters[domain]

    if robot_parser is None:
        return True

    return robot_parser.can_fetch('*', url)


def _get_robot(url: str) -> RobotFileParser:
    robot_file_url = _get_robot_file_url(url)

    try:
        robot_parser = RobotFileParser(robot_file_url)
        robot_parser.read()
    except Exception:
        robot_parser = None

    return robot_parser


def _get_robot_file_url(url: str) -> str:
    return urlparse(url)._replace(path='robots.txt', params='', query='', fragment='').geturl()
