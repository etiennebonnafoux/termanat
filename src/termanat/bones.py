"""Reference data for the bones drawn on the skeleton.

Language-independent data (key, Latin name) lives here. The texts live in one
module per language (``bones_en``, ``bones_fr``) so that each translation can be
proofread on its own.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class BoneText:
    """Everything about a bone that depends on the language."""

    name: str
    region: str
    count: str
    kind: str  # long, short, flat, irregular, sesamoid...
    description: str
    landmarks: list[str]
    joints: list[str]
    clinical: list[str]
    fact: str
    old_names: list[str] = field(default_factory=list)  # former nomenclature


@dataclass(frozen=True)
class Bone:
    key: str  # one-letter id used in the skeleton mask
    latin: str  # Terminologia Anatomica
    texts: dict[str, BoneText]

    def text(self, lang: str) -> BoneText:
        return self.texts[lang]

    def name(self, lang: str) -> str:
        return self.texts[lang].name


# Order of the list in the app: head to feet.
_ORDER = [
    ("S", "Cranium"),
    ("M", "Mandibula"),
    ("C", "Vertebrae cervicales"),
    ("X", "Scapula"),
    ("L", "Clavicula"),
    ("T", "Sternum"),
    ("R", "Costae"),
    ("H", "Humerus"),
    ("D", "Radius"),
    ("U", "Ulna"),
    ("A", "Ossa manus"),
    ("V", "Vertebrae lumbales"),
    ("Y", "Os sacrum et os coccygis"),
    ("P", "Os coxae"),
    ("F", "Femur"),
    ("K", "Patella"),
    ("B", "Tibia"),
    ("I", "Fibula"),
    ("O", "Ossa pedis"),
]


def _load() -> list[Bone]:
    from .bones_en import TEXTS as EN
    from .bones_fr import TEXTS as FR

    return [Bone(key, latin, {"en": EN[key], "fr": FR[key]}) for key, latin in _ORDER]


BONES: list[Bone] = _load()
BY_KEY: dict[str, Bone] = {b.key: b for b in BONES}
