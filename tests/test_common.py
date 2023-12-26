"""Common tests."""

# ruff: noqa: S101

from __future__ import annotations

from vanctransit.common import LOSDevice


def test_losdevice() -> None:
    """Test the LOSDevice class."""
    device = LOSDevice("NewType")
    assert device.new_type == "NewType"
    assert device.create() == "FOO"
