"""A component for handling domain and robots.txt filters."""


from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

import tldextract

import domain_filters
import robot_filters


def filter_urls(urls: list[str]) -> list[str]:
    """Filter URLs based on domain and robots.txt filters"""
    return list(filter(_check_url, urls))


def _check_url(url: str) -> bool:
    """Check the URL according to domain and robots.txt filters.

    Args:
        url (str): The URL.

    Returns:
        bool: True if the URL passes through the filters.
    """
    return _check_domain_filters(url) and _check_robot_filters(url)


def _check_domain_filters(url: str) -> bool:
    """Check the URL according to domain filters.

    Args:
        url (str): The URL.

    Returns:
        bool: True if the URL passes through the domain filters.
    """
    extracted_url = tldextract.extract(url)
    domain = '.'.join(extracted_url)
    base_domain = extracted_url.registered_domain

    if domain_filters.empty():
        return True

    return domain_filters.contains(domain) or domain_filters.contains(base_domain)


def _check_robot_filters(url: str) -> bool:
    """Check the URL according to the robot filters.

    Args:
        url (str): The URL.

    Returns:
        bool: True if the URL passes through the robot filters.
    """
    domain = '.'.join(tldextract.extract(url))

    if not robot_filters.contains(domain):
        robot_filters.add(domain, _get_robot_parser(url))

    robot_parser = robot_filters.get_robot_parser(domain)

    if robot_parser is None:
        return True

    return robot_parser.can_fetch('*', url)


def _get_robot_parser(url: str) -> RobotFileParser | None:
    """Get a RobotFileParser for given URL.

    Args:
        url (str): The URL.

    Returns:
        RobotFileParser: The RobotFileParser object.
    """
    robot_file_url = _get_robot_file_url(url)

    try:
        robot_parser = RobotFileParser(robot_file_url)
        robot_parser.read()
    except Exception:
        robot_parser = None

    return robot_parser


def _get_robot_file_url(url: str) -> str:
    """Get the robots.txt URL based on the given URL.

    Args:
        url (str): The URL.

    Returns:
        str: The robots.txt URL.
    """
    return urlparse(url)._replace(path='robots.txt', params='', query='', fragment='').geturl()
