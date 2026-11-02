"""The nervous system (anterior view, schematic)."""

from __future__ import annotations

from ...model import Structure, System
from .art import ART, MASK
from .texts_en import TEXTS as EN
from .texts_fr import TEXTS as FR

# Display order (central, then peripheral from head to feet) and Latin names
# (Terminologia Anatomica).
_ORDER = [
    ("B", "Cerebrum"),
    ("C", "Cerebellum"),
    ("T", "Truncus encephali"),
    ("M", "Medulla spinalis"),
    ("Q", "Cauda equina"),
    ("V", "Nervus vagus"),
    ("P", "Nervus phrenicus"),
    ("X", "Plexus brachialis"),
    ("K", "Nervus musculocutaneus"),
    ("R", "Nervus radialis"),
    ("D", "Nervus medianus"),
    ("U", "Nervus ulnaris"),
    ("I", "Nervi intercostales"),
    ("F", "Nervus femoralis"),
    ("S", "Nervus ischiadicus"),
    ("N", "Nervus tibialis"),
    ("G", "Nervus fibularis communis"),
]

# Muted resting colours: CNS in pinks / violets, peripheral nerves in yellows,
# neighbours (the arm nerves side by side) kept distinguishable.
_COLORS = {
    "B": "#af8787",
    "C": "#af87af",
    "T": "#8787af",
    "M": "#87afaf",
    "Q": "#87af87",
    "V": "#5fafaf",
    "P": "#5f87af",
    "X": "#d7d787",
    "K": "#87af5f",
    "R": "#d7af5f",
    "D": "#afaf5f",
    "U": "#d7875f",
    "I": "#af875f",
    "F": "#afd75f",
    "S": "#d7af87",
    "N": "#afaf87",
    "G": "#d78787",
}

SYSTEM = System(
    id="nervous",
    names={"en": "Nervous system", "fr": "Système nerveux"},
    art=ART,
    mask=MASK,
    structures=[
        Structure(key, latin, {"en": EN[key], "fr": FR[key]}) for key, latin in _ORDER
    ],
    colors=_COLORS,
)
