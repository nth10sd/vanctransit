"""Begin running package code."""

from __future__ import annotations

from logging import INFO as INFO_LOG_LEVEL
from typing import cast

import osmnx as ox

# pylint: disable=no-name-in-module
# pyrefly: ignore  # import-error
from vanctransit._vanctransit import (
    print_something,  # pyright: ignore[reportUnknownVariableType]
)
# pyrefly: ignore  # import-error
from vanctransit._vanctransit import (
    sum_as_string,  # pyright: ignore[reportUnknownVariableType]
)
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
    result: str = cast("str", sum_as_string(2, 3))
    RUN_LOG.info(result)

    _ = ox.plot_graph(  # pyright: ignore[reportUnknownMemberType]
        ox.graph_from_place(  # pyright: ignore[reportUnknownMemberType]
            "Vancouver, British Columbia", network_type="walk"
        )
    )
