"""The main superficial skeletal muscles (anterior view)."""

from __future__ import annotations

from ...model import Structure, System
from .art import ART, MASK
from .texts_en import TEXTS as EN
from .texts_fr import TEXTS as FR

# Display order (head to feet) and Latin names (Terminologia Anatomica).
_ORDER = [
    ("N", "Musculus sternocleidomastoideus"),
    ("T", "Musculus trapezius"),
    ("D", "Musculus deltoideus"),
    ("P", "Musculus pectoralis major"),
    ("S", "Musculus serratus anterior"),
    ("B", "Musculus biceps brachii"),
    ("R", "Musculus brachioradialis"),
    ("F", "Musculi flexores antebrachii superficiales"),
    ("A", "Musculus rectus abdominis"),
    ("O", "Musculus obliquus externus abdominis"),
    ("Z", "Musculus sartorius"),
    ("Q", "Musculus quadriceps femoris"),
    ("G", "Musculi adductores femoris"),
    ("J", "Musculus tibialis anterior"),
    ("L", "Musculus fibularis longus"),
    ("C", "Musculus triceps surae"),
]

# Muted resting colours; neighbouring muscles get slightly different tones.
_RED = "#a86a6a"
_ROSE = "#b88080"
_BROWN = "#9a7060"
_PLUM = "#9a6878"

SYSTEM = System(
    id="muscles",
    names={"en": "Muscles", "fr": "Muscles"},
    art=ART,
    mask=MASK,
    structures=[
        Structure(key, latin, {"en": EN[key], "fr": FR[key]}) for key, latin in _ORDER
    ],
    colors={
        "N": _ROSE,
        "T": _BROWN,
        "D": _RED,
        "P": _ROSE,
        "S": _BROWN,
        "B": _ROSE,
        "R": _BROWN,
        "F": _PLUM,
        "A": _RED,
        "O": _PLUM,
        "Z": _BROWN,
        "Q": _RED,
        "G": _PLUM,
        "J": _RED,
        "L": _BROWN,
        "C": _PLUM,
    },
)
