"""Smoke tests for the installable package."""

from importlib.metadata import version

from quantumshield import __version__


def test_version_is_public_and_well_formed() -> None:
    parts = __version__.split(".")
    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)


def test_version_matches_installed_metadata() -> None:
    assert __version__ == version("quantumshield")
