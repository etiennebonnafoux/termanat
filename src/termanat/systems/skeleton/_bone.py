"""Keeps the bone texts short to write: a bone always has the same sections."""

from __future__ import annotations

from ...model import StructureText


def BoneText(  # noqa: N802 - reads like the dataclass it builds
    *,
    name: str,
    region: str,
    count: str,
    kind: str,
    description: str,
    landmarks: list[str],
    joints: list[str],
    clinical: list[str],
    fact: str,
    old_names: list[str] | None = None,
) -> StructureText:
    return StructureText(
        name=name,
        kind=kind,
        region=region,
        description=description,
        sections={"landmarks": landmarks, "joints": joints, "clinical": clinical},
        fact=fact,
        count=count,
        old_names=old_names or [],
    )
