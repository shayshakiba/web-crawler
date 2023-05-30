"""A component for storing robot filters.

This module acts as a singleton resource.
"""


from urllib.robotparser import RobotFileParser


_robot_filters: dict[str, RobotFileParser] = dict()


def add(domain: str, robot_parser: RobotFileParser) -> None:
    _robot_filters[domain] = robot_parser


def get_robot_parser(domain: str) -> RobotFileParser | None:
    if not domain in _robot_filters:
        return None

    return _robot_filters[domain]


def contains(domain: str) -> bool:
    return domain in _robot_filters
