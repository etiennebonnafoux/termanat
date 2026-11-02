"""termanat: discover and learn anatomy inside your terminal."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("termanat")
except PackageNotFoundError:  # pragma: no cover - running from a source tree
    __version__ = "0.0.0"


def main() -> None:
    from .app import main as _main

    _main()
