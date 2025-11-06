"""Begin running package code."""

from __future__ import annotations

from logging import INFO as INFO_LOG_LEVEL
from typing import cast

# pylint: disable=no-name-in-module
# import-error  # noqa: ERA001,RUF100
# pylint: disable=line-too-long
from vanctransit._vanctransit import (  # ty: ignore[unresolved-import]  # pyrefly: ignore[missing-import]
    print_something,  # pyright: ignore[reportUnknownVariableType]
)

# import-error  # noqa: ERA001,RUF100
# pylint: disable=line-too-long
from vanctransit._vanctransit import (  # ty: ignore[unresolved-import]  # pyrefly: ignore[missing-import]
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

    # \_ = ox.plot_graph(  # p yright: ignore[reportUnknownMemberType]
    # \    ox.graph_from_place(  # p yright: ignore[reportUnknownMemberType]
    # \        "Vancouver, British Columbia", network_type="walk"
    # \    )
    # \)
