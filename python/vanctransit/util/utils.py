"""Place utility functions here."""

from __future__ import annotations

import logging

from vanctransit.util.logging import get_logger

UTIL_RUN_LOG: logging.Logger = get_logger(__name__, fmt="%(message)s")
UTIL_RUN_LOG.setLevel(logging.INFO)


def add_one(inp: int) -> int:
    """Return input added one.

    :param inp: Input number
    :return: Input added one
    """
    UTIL_RUN_LOG.info("Adding one...")
    return inp + 1
