"""Circulation: the heart and main vessels (anterior view)."""

from __future__ import annotations

from ...model import Structure, System
from .art import ART, MASK
from .texts_en import TEXTS as EN
from .texts_fr import TEXTS as FR

# Display order (heart, then head to feet) and Latin names (Terminologia Anatomica).
_ORDER = [
    ("H", "Cor"),
    ("A", "Aorta ascendens et arcus aortae"),
    ("P", "Truncus pulmonalis"),
    ("S", "Vena cava superior"),
    ("C", "Arteria carotis communis"),
    ("J", "Vena jugularis interna"),
    ("U", "Arteria subclavia"),
    ("X", "Arteria brachialis"),
    ("R", "Arteria radialis"),
    ("N", "Arteria ulnaris"),
    ("B", "Pars abdominalis aortae"),
    ("I", "Vena cava inferior"),
    ("T", "Truncus coeliacus"),
    ("K", "Arteria renalis"),
    ("L", "Arteria iliaca communis"),
    ("F", "Arteria femoralis"),
    ("G", "Arteria poplitea"),
    ("V", "Vena saphena magna"),
]

_ARTERY = "#a85f5f"  # muted red
_VEIN = "#5f7fa8"  # muted blue

SYSTEM = System(
    id="circulatory",
    names={"en": "Circulation", "fr": "Circulation sanguine"},
    art=ART,
    mask=MASK,
    structures=[
        Structure(key, latin, {"en": EN[key], "fr": FR[key]}) for key, latin in _ORDER
    ],
    colors={
        "H": "#a8646e",  # muscle red
        "P": "#7f6fa8",  # artery carrying oxygen-poor blood: blue-violet
        **{k: _ARTERY for k in "ACUXRNBTKLFG"},
        **{k: _VEIN for k in "SIJV"},
    },
)
