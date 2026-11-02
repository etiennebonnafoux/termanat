"""The skeleton (anterior view)."""

from __future__ import annotations

from ...model import Structure, System
from .art import ART, MASK
from .texts_en import TEXTS as EN
from .texts_fr import TEXTS as FR

# Display order (head to feet) and Latin names (Terminologia Anatomica).
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

SYSTEM = System(
    id="skeleton",
    names={"en": "Skeleton", "fr": "Squelette"},
    art=ART,
    mask=MASK,
    structures=[
        Structure(key, latin, {"en": EN[key], "fr": FR[key]}) for key, latin in _ORDER
    ],
)
