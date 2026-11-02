"""ASCII art of the human skeleton (anterior view).

The drawing is authored as the *left half* plus a center column and mirrored
(see :func:`termanat.model.build_mirrored`), which keeps the skeleton symmetric
and highlights every bone on both sides of the body.

The figure is in anatomical position and seen from the front, so the left half
of the screen is the subject's *right* side.
"""

from __future__ import annotations

from ...model import build_mirrored

HALF_WIDTH = 20


def _rib(n: int) -> tuple[int, str, str]:
    """A rib row: ``n`` rib characters ending next to the sternum."""
    return (HALF_WIDTH - n - 2, "=" * n + "\\_", "R")


_ARM = 7  # column of the humerus / forearm
_HAND = 6
_LEG = 15  # column of the femur / tibia / fibula

_ROWS: list[tuple[list[tuple[int, str, str]], str, str]] = [
    # skull
    ([(14, '.-""""', "S")], '"', "S"),
    ([(13, "/", "S")], " ", " "),
    ([(13, "|", "S"), (16, ".-.", "S")], " ", " "),
    ([(13, "|", "S"), (16, "'-'", "S")], " ", " "),
    ([(13, "\\", "S")], "^", "S"),
    ([(14, "\\,,,,,", "S")], ",", "S"),
    # mandible
    ([(15, "|''''", "M")], "'", "M"),
    ([(16, "\\___", "M")], "_", "M"),
    # neck & shoulder girdle
    ([], "#", "C"),
    ([(_ARM, ".__", "X"), (_ARM + 3, ".--------'", "L")], "#", "C"),
    # thorax + upper arm
    ([(_ARM, "(__", "H"), _rib(3)], "|", "T"),
    ([(_ARM, "| |", "H"), _rib(5)], "|", "T"),
    ([(_ARM, "| |", "H"), _rib(6)], "|", "T"),
    ([(_ARM, "| |", "H"), _rib(5)], "|", "T"),
    ([(_ARM, "| |", "H"), _rib(4)], "v", "T"),
    ([(_ARM, "| |", "H"), (15, "==\\", "R")], "#", "V"),
    ([(_ARM, "|_|", "H")], "#", "V"),
    # forearm (radius on the thumb / outer side, ulna on the inner side) + pelvis
    ([(_ARM, "/ \\", "D U")], "#", "V"),
    ([(_ARM, "| |", "D U"), (16, "_.-'", "P")], "#", "V"),
    ([(_ARM, "| |", "D U"), (15, "/  .-", "P  YY")], "-", "Y"),
    ([(_ARM, "| |", "D U"), (15, "\\  \\ ", "P  Y ")], "#", "Y"),
    ([(_ARM, "| |", "D U"), (16, "'._\\", "PPPY")], "v", "Y"),
    # hands + thighs
    ([(_ARM, "{=}", "A"), (_LEG, "| |", "F")], " ", " "),
    ([(_HAND, "{###}", "A"), (_LEG, "| |", "F")], " ", " "),
    ([(_HAND, "|||||", "A"), (_LEG, "| |", "F")], " ", " "),
    ([(_HAND, "'''''", "A"), (_LEG, "| |", "F")], " ", " "),
    ([(_LEG, "| |", "F")], " ", " "),
    ([(_LEG, "| |", "F")], " ", " "),
    ([(_LEG, "|_|", "F")], " ", " "),
    # knee
    ([(_LEG, "(_)", "K")], " ", " "),
    # leg (fibula on the outer side, tibia on the inner side)
    ([(_LEG, "| |", "I B")], " ", " "),
    ([(_LEG, "| |", "I B")], " ", " "),
    ([(_LEG, "| |", "I B")], " ", " "),
    ([(_LEG, "| |", "I B")], " ", " "),
    ([(_LEG, "|_|", "IBB")], " ", " "),
    # feet
    ([(_LEG - 1, "/###\\", "O")], " ", " "),
    ([(_LEG - 2, "(_____)", "O")], " ", " "),
]


ART, MASK = build_mirrored(_ROWS, HALF_WIDTH)
