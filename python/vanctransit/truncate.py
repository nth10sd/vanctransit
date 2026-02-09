"""Sample code involving truncation."""

from collections import deque
from itertools import islice
from pathlib import Path
from typing import TYPE_CHECKING
from typing import Any

# pylint: disable=no-name-in-module
# import-error  # noqa: ERA001,RUF100
# pylint: disable=line-too-long
from vanctransit._vanctransit import (  # ty: ignore[unresolved-import]  # pyrefly: ignore[missing-import]
    truncate_file_lines,  # pyright: ignore[reportUnknownVariableType]
)

if TYPE_CHECKING:
    from collections.abc import Callable
    from collections.abc import Iterable


def py_truncate_file_lines(  # vulture: ignore
    filename: Path | str, lines_wanted: int
) -> None:
    """Truncate files to desired number of lines, similar algorithm to naive Rust one.

    :param filename: Filename of file to truncate
    :param lines_wanted: Desired number of lines to retain
    """
    temp_file = Path(filename).with_suffix("").with_suffix(f"{Path(filename).suffix}~")
    with (
        Path(filename).open(encoding="utf-8") as f,
        temp_file.open("w", encoding="utf-8") as g,
    ):
        for idx, line in enumerate(f.readlines()):
            if idx >= lines_wanted:
                break
            _ = g.write(line)

    target_file = temp_file.with_suffix("").with_suffix(
        str(Path(filename).suffix.removesuffix("~"))
    )
    # Needs to be opened in binary mode or else Windows uses CRLF instead of LF
    with temp_file.open("rb") as f, target_file.open("wb") as g:
        g.writelines(line.replace(b"\r\n", b"\n") for line in f)
    temp_file.unlink()


def fast_py_truncate_file_lines(  # vulture: ignore
    filename: Path | str, lines_wanted: int
) -> None:
    """Truncate files to desired number of lines, optimized algorithm in Python.

    Adapted from https://stackoverflow.com/a/27672002

    :param filename: Filename of file to truncate
    :param lines_wanted: Desired number of lines to retain
    """
    with Path(filename).open("r+", encoding="utf-8", errors="surrogateescape") as f:
        # pylint: disable-next=line-too-long
        blackhole: Callable[[Iterable[Any]], None]  # type: ignore[explicit-any]  # ty: ignore[unused-ignore-comment]  # pyright: ignore[reportExplicitAny]
        blackhole = deque(maxlen=0).extend
        file_iterator = iter(f.readline, "")
        blackhole(
            islice(  # type: ignore[arg-type]  # ty: ignore[invalid-argument-type]
                file_iterator,
                lines_wanted,
            )
        )
        _ = f.truncate(f.tell())


def sample_truncation() -> None:
    """Sample truncation."""
    root_folder = Path(__file__).parents[2]
    desired_file = root_folder / "enwik9.txt"

    if desired_file.is_file():
        # Swap this with py_truncate_file_lines or vice versa
        truncate_file_lines(desired_file, 100000)


sample_truncation()
