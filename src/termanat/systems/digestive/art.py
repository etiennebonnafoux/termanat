"""ASCII art of the digestive system (anterior view).

The figure is in anatomical position and seen from the front: the left of the
screen is the subject's *right* side (liver, gallbladder, caecum and appendix
on the left of the screen; stomach, descending and sigmoid colon on the right).

It is authored as placements ``(row, column, text, key)`` on a blank canvas:
every non-space character of ``text`` gets ``key`` in the mask (spaces are
transparent). The ``.`` key (``OUTLINE``) draws the faint body silhouette.
The colon is drawn as a chain of haustra ``[]``.
"""

from __future__ import annotations

from ...model import OUTLINE

WIDTH = 41
HEIGHT = 37

_O = OUTLINE

_PLACEMENTS: list[tuple[int, int, str, str]] = [
    # --- silhouette: head, neck, shoulders --------------------------------
    (0, 14, '.-"""""""""-.', _O),
    (1, 13, "/", _O), (1, 27, "\\", _O),
    (2, 12, "(", _O), (2, 28, ")", _O),
    (3, 13, "|", _O), (3, 27, "|", _O),
    (4, 13, "\\", _O), (4, 27, "/", _O),
    (5, 14, "\\", _O), (5, 26, "/", _O),
    (6, 15, "'-.", _O), (6, 23, ".-'", _O),
    (7, 17, "|", _O), (7, 23, "|", _O),
    (8, 3, ".-------------'", _O), (8, 23, "'-------------.", _O),
    (9, 2, "/", _O), (9, 38, "\\", _O),
]
for _r in range(10, 32):  # sides of the trunk
    _PLACEMENTS += [(_r, 1, "|", _O), (_r, 39, "|", _O)]
_PLACEMENTS += [  # hips converging to the perineum
    (32, 2, "\\", _O), (32, 38, "/", _O),
    (33, 3, "\\", _O), (33, 37, "/", _O),
    (34, 4, "'.", _O), (34, 35, ".'", _O),
    (35, 6, "'-.", _O), (35, 32, ".-'", _O),
    (36, 9, "'--..", _O), (36, 27, "..--'", _O),
]

_PLACEMENTS += [
    # --- head and neck ------------------------------------------------------
    # parotid glands in front of the ears, parotid ducts towards the cheeks
    (2, 13, "@@", "P"), (2, 26, "@@", "P"),
    (3, 14, "@@-", "P"), (3, 24, "-@@", "P"),
    # oral cavity: upper teeth, tongue, lower teeth
    (3, 17, ".vvvvv.", "O"),
    (4, 17, "(~~~~~)", "O"),
    (5, 17, "'^^^^^'", "O"),
    # pharynx
    (6, 18, "\\:::/", "H"),
    (7, 19, "\\:/", "H"),
    # oesophagus, deviating to the subject's left towards the cardia
    (8, 19, "|:|", "E"),
    (9, 19, "|:|", "E"),
    (10, 19, "|:|", "E"),
    (11, 20, "\\:\\", "E"),
    (12, 21, "\\:\\", "E"),
    # --- liver and gallbladder (left of screen = subject's right) ------------
    (12, 4, '_.-"""""""""-._', "L"),
    (13, 3, "/#################\\", "L"),
    (14, 2, "(##################/", "L"),
    (15, 2, "\\################/", "L"),
    (16, 3, "\\##############/", "L"),
    (17, 4, "'-.", "L"), (17, 11, "##.-'", "L"),
    (17, 7, "(__)", "G"),
    # --- stomach --------------------------------------------------------------
    (12, 25, "_.--._", "S"),
    (13, 23, ".'::::::'.", "S"),
    (14, 23, "|:::::::::\\", "S"),
    (15, 23, "|::::::::::|", "S"),
    (16, 22, "/::::::::::/", "S"),
    (17, 18, "_.-'::::::::/", "S"),
    (18, 16, "=(::::::::.-'", "S"),
    (19, 17, "'-....-'", "S"),
    # --- duodenum (C-shaped) and pancreas (head in the C, tail to the spleen) -
    (18, 8, ".=======", "D"),
    (19, 8, "||", "D"),
    (20, 8, "||", "D"),
    (21, 8, "||", "D"),
    (22, 8, "||", "D"),
    (23, 8, "\\\\==========//", "D"),
    (22, 21, "//", "D"),
    (21, 22, "|'", "D"),
    (19, 11, ".~~.", "N"),
    (20, 10, "(~~~~~~~~~~~~~~~~~~~~~~~~>", "N"),
    (21, 11, "(~~~)", "N"),
    (22, 11, "'~~'", "N"),
    # --- large intestine ------------------------------------------------------
    # transverse colon, sagging between the right and left colic flexures
    (24, 5, "[][][]", "T"), (24, 29, "[][]", "T"), (23, 33, "[]", "T"),
    (25, 11, "[][][][][][][][][]", "T"),
    # ascending colon (subject's right) from the caecum to the right flexure
    (24, 3, ".-", "A"),
]
for _r in range(25, 30):
    _PLACEMENTS.append((_r, 3, "[]", "A"))
_PLACEMENTS += [
    # caecum and vermiform appendix
    (30, 2, "(::)", "C"),
    (31, 2, "\\__/", "C"),
    (32, 5, "\\)", "C"),
    # descending colon (subject's left) from the left flexure
    (22, 34, ".-.", "X"), (23, 35, "[]", "X"), (24, 35, "[]", "X"),
]
for _r in range(25, 31):
    _PLACEMENTS.append((_r, 35, "[]", "X"))
_PLACEMENTS += [
    # sigmoid colon, looping down into the pelvis
    (31, 32, "[][]", "Z"),
    (32, 22, "[][][][][]", "Z"),
    # rectum (ampulla) and anal canal
    (32, 18, "(::)", "R"),
    (33, 18, "(::)", "R"),
    (34, 18, "\\::/", "R"),
    (35, 19, "||", "R"),
    # small intestine: jejunum and ileum, the terminal ileum joining the caecum
    (26, 10, ".@~@~@~@~@~@~@~@~@~@.", "J"),
    (27, 8, "(@~@~@~@~@~@~@~@~@~@~@~)", "J"),
    (28, 8, "(~@~@~@~@~@~@~@~@~@~@~@)", "J"),
    (29, 9, "'@~@~@~@~@~@~@~@~@~@~'", "J"),
    (30, 6, "=='-@~@~@~@~@~@~@-'", "J"),
]


def _render() -> tuple[list[str], list[str]]:
    art = [[" "] * WIDTH for _ in range(HEIGHT)]
    mask = [[" "] * WIDTH for _ in range(HEIGHT)]
    for row, col, text, key in _PLACEMENTS:
        for i, ch in enumerate(text):
            if ch == " ":
                continue
            if art[row][col + i] != " ":
                raise ValueError(f"overlap at row {row}, column {col + i} ({text!r})")
            art[row][col + i] = ch
            mask[row][col + i] = key
    return ["".join(r).rstrip() for r in art], ["".join(r).rstrip() for r in mask]


ART, MASK = _render()
