"""The digestive system (anterior view)."""

from __future__ import annotations

from ...model import Structure, System
from .art import ART, MASK
from .texts_en import TEXTS as EN
from .texts_fr import TEXTS as FR

# Display order (mouth to anus, accessory glands next to their segment) and
# Latin names (Terminologia Anatomica).
_ORDER = [
    ("O", "Cavitas oris"),
    ("P", "Glandula parotidea"),
    ("H", "Pharynx"),
    ("E", "Oesophagus"),
    ("S", "Gaster"),
    ("D", "Duodenum"),
    ("L", "Hepar"),
    ("G", "Vesica biliaris et ductus biliares extrahepatici"),
    ("N", "Pancreas"),
    ("J", "Jejunum et ileum"),
    ("C", "Caecum et appendix vermiformis"),
    ("A", "Colon ascendens"),
    ("T", "Colon transversum"),
    ("X", "Colon descendens"),
    ("Z", "Colon sigmoideum"),
    ("R", "Rectum et canalis analis"),
]

# Muted resting colours: digestive tube pinkish, glands tan, liver brown,
# bile green, colon brownish.
_COLORS = {
    "O": "#c08a8a",
    "P": "#a596b8",
    "H": "#b88484",
    "E": "#b07c7c",
    "S": "#c49090",
    "D": "#bf9a72",
    "L": "#9c5f52",
    "G": "#7f9a5c",
    "N": "#c8a77e",
    "J": "#c98d86",
    "C": "#a98b68",
    "A": "#a98b68",
    "T": "#a98b68",
    "X": "#a98b68",
    "Z": "#a98b68",
    "R": "#a07868",
}

SYSTEM = System(
    id="digestive",
    names={"en": "Digestive system", "fr": "Appareil digestif"},
    art=ART,
    mask=MASK,
    structures=[
        Structure(key, latin, {"en": EN[key], "fr": FR[key]}) for key, latin in _ORDER
    ],
    colors=_COLORS,
)
