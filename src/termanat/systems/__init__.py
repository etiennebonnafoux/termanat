"""Registry of body systems, in the order shown in the app.

Each system is a subpackage exposing ``SYSTEM`` (a :class:`termanat.model.System`).
"""

from __future__ import annotations

from importlib import import_module

from ..model import System

_IDS = ["skeleton", "muscles", "digestive", "circulatory", "nervous"]


def _load() -> list[System]:
    systems = []
    for sid in _IDS:
        try:
            module = import_module(f"{__name__}.{sid}")
        except ModuleNotFoundError as exc:  # not written yet
            if exc.name != f"{__name__}.{sid}":
                raise
            continue
        systems.append(module.SYSTEM)
    return systems


SYSTEMS: list[System] = _load()
BY_ID: dict[str, System] = {s.id: s for s in SYSTEMS}
