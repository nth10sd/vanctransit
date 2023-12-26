"""Begin running package code."""

from __future__ import annotations

from logging import INFO as INFO_LOG_LEVEL

import osmnx as ox

# pylint: disable=no-name-in-module
from vanctransit._vanctransit import print_something
from vanctransit._vanctransit import sum_as_string
from vanctransit.util.logging import get_logger
from vanctransit.util.utils import add_one

RUN_LOG = get_logger(__name__)
RUN_LOG.setLevel(INFO_LOG_LEVEL)


def main() -> None:
    """Start."""
    RUN_LOG.warning(add_one(2))
    RUN_LOG.error("foo")

    RUN_LOG.info("Rust functions below:")
    print_something()
    RUN_LOG.info(sum_as_string(2, 3))

    ox.plot_graph(
        ox.graph_from_place("Vancouver, British Columbia", network_type="walk")
    )
