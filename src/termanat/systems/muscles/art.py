"""ASCII art of the main superficial skeletal muscles (anterior view).

The drawing is authored as the *left half* plus a center column and mirrored
(see :func:`termanat.model.build_mirrored`), so every muscle is highlighted on
both sides of the body.

The figure is in anatomical position and seen from the front: the left half of
the screen is the subject's *right* side, and "lateral" is toward the screen
edge. Muscle fills follow the main fibre direction where possible. The head,
sternum, linea alba, hands, knees, tibial shaft and feet are a dimmed outline.
"""

from __future__ import annotations

from ...model import OUTLINE, build_mirrored

HALF_WIDTH = 20

# Each row: (left-half art, left-half mask, center char, center mask).
# Mask keys: N sternocleidomastoid, T trapezius, D deltoid, P pectoralis major,
# S serratus anterior, B biceps brachii, R brachioradialis, F forearm flexors,
# A rectus abdominis, O external oblique, Z sartorius, Q quadriceps,
# G adductors, J tibialis anterior, L fibularis longus, C triceps surae,
# "." outline.
_O = OUTLINE
_ROWS_SRC: list[tuple[str, str, str, str]] = [
    # head (outline)
    (r'                .-""', r"                ....", '"', _O),
    (r"               /    ", r"               .    ", " ", " "),
    (r"               \    ", r"               .    ", " ", " "),
    (r"                '.__", r"                ....", "_", _O),
    # neck: sternocleidomastoid + upper trapezius
    (r"             _.-'\\ ", r"             TTTTNN ", " ", " "),
    (r"        _.-~~~~~~~\\", r"        TTTTTTTTTTNN", " ", " "),
    # shoulder, chest
    (r"    .-::::========= ", r"    DDDDDDPPPPPPPPP ", "|", _O),
    (r"   /:::::\==========", r"   DDDDDDPPPPPPPPPPP", "|", _O),
    (r"   |:::::|\=========", r"   DDDDDDPPPPPPPPPPP", "|", _O),
    (r"   |::::/  \========", r"   DDDDDD  PPPPPPPPP", "|", _O),
    (r"    \::/ >> \_______", r"    DDDD SS PPPPPPPP", "|", _O),
    # arm, abdomen
    (r"   (##)  >>\\\\\[##", r"   BBBB  SSOOOOOAAA", "|", _O),
    (r"   (##)  >>\\\\\[==", r"   BBBB  SSOOOOOAAA", "|", _O),
    (r"   (##)  >>\\\\\[##", r"   BBBB  SSOOOOOAAA", "|", _O),
    (r"   (##)  \\\\\\\[==", r"   BBBB  OOOOOOOAAA", "|", _O),
    (r"   (##)  \\\\\\\[##", r"   BBBB  OOOOOOOAAA", "|", _O),
    (r"   \##/   \\\\\\[==", r"   BBBB   OOOOOOAAA", "|", _O),
    # forearm
    (r"  /(:::\   \\\\\[##", r"  RRFFFF   OOOOOAAA", "|", _O),
    (r"  ((:::    \\\\\[##", r"  RRFFF    OOOOOAAA", "|", _O),
    (r"  ((:::     \\\\[##", r"  RRFFF     OOOOAAA", "|", _O),
    (r"  ((:::      \\\[##", r"  RRFFF      OOOAAA", "|", _O),
    (r"  |(::|       \\\##", r"  RRFFF       OOOAA", "|", _O),
    # hands + thighs (femoral triangle left empty between Z and G)
    (r"  .,,,.  |\\  /////", r"  .....  QZZ  GGGGG", " ", " "),
    (r" (|||||  ||\\ /////", r" ......  QQZZ GGGGG", " ", " "),
    (r"  '|||'  |||\\////", r"  .....  QQQZZGGGG", " ", " "),
    (r"   '''   ||||\\///", r"   ...   QQQQZZGGG", " ", " "),
    (r"         ||||\\///", r"         QQQQZZGGG", " ", " "),
    (r"         |||||\\//", r"         QQQQQZZGG", " ", " "),
    (r"         ||||||\\/", r"         QQQQQQZZG", " ", " "),
    (r"          \||||\\", r"          QQQQQZZ", " ", " "),
    # knee (patella outline) + medial insertion of the sartorius
    (r"           (__)\ ", r"           ....Z ", " ", " "),
    # leg
    (r"          ::||!)) ", r"          LLJJ.CC ", " ", " "),
    (r"          ::||!)) ", r"          LLJJ.CC ", " ", " "),
    (r"           :||!) ", r"           LJJ.C ", " ", " "),
    (r"           :||!) ", r"           LJJ.C ", " ", " "),
    (r"           :||!) ", r"           LJJ.C ", " ", " "),
    # foot (outline)
    (r"         _/___\ ", r"         ...... ", " ", " "),
]

_ROWS = [([(0, art, mask)], c, cm) for art, mask, c, cm in _ROWS_SRC]

ART, MASK = build_mirrored(_ROWS, HALF_WIDTH)
