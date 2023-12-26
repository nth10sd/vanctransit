"""Begin running package code."""

from __future__ import annotations

from logging import INFO as INFO_LOG_LEVEL

from vanctransit.common import LOSDevice
from vanctransit.util.logging import get_logger
from vanctransit.util.utils import add_one

RUN_LOG = get_logger(__name__)
RUN_LOG.setLevel(INFO_LOG_LEVEL)


def main() -> None:
    """Start."""
    LOSDevice("NewType")
    RUN_LOG.warning(add_one(2))
    RUN_LOG.error("foo")
