"""Module details."""

import contextlib

with contextlib.suppress(ModuleNotFoundError):  # Bypass package install issues on CI
    from beartype import BeartypeConf
    from beartype.claw import beartype_this_package

__title__ = "vanctransit"
__version__ = "0.1.0"

with contextlib.suppress(NameError):
    beartype_this_package(  # pyright: ignore[reportPossiblyUnboundVariable]
        conf=BeartypeConf(  # pyright: ignore[reportPossiblyUnboundVariable]
            violation_type=UserWarning
        )
    )
