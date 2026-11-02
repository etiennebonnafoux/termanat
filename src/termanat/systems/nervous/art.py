"""ASCII art of the nervous system (anterior view, schematic).

Authored as the *left half* plus a center column and mirrored (see
:func:`termanat.model.build_mirrored`). The left half of the screen is the
subject's *right* side. A faint body silhouette (``.``) gives the landmarks.

Keys: B cerebrum, C cerebellum, T brainstem, M spinal cord, Q cauda equina,
V vagus nerve, P phrenic nerve, X brachial plexus, K musculocutaneous nerve,
R radial nerve, D median nerve, U ulnar nerve, I intercostal nerves,
F femoral nerve (lumbar plexus), S sciatic nerve (sacral plexus),
N tibial nerve, G common fibular nerve.
"""

from __future__ import annotations

from ...model import build_mirrored

HALF_WIDTH = 20

_ROWS: list[tuple[list[tuple[int, str, str]], str, str]] = [
    # cerebrum (two hemispheres separated by the longitudinal fissure)
    ([(14, "_.-~~~", "B")], "_", "B"),
    ([(12, ".~~~~~~~", "B")], "|", "B"),
    ([(11, "(~~~~~~~~", "B")], "|", "B"),
    ([(11, "(~~~~~~~~", "B")], "|", "B"),
    ([(11, "(~~~~~~~~", "B")], "|", "B"),
    ([(12, "'~~~~~~~", "B")], "|", "B"),
    ([(13, "'-~~~~", "B")], "^", "B"),
    # cerebellum beside the brainstem (schematic: it lies behind)
    ([(15, "(@@@", "C"), (19, "[", "T")], "#", "T"),
    ([(16, "'@@", "C"), (19, "[", "T")], "#", "T"),
    # neck: phrenic (on the anterior scalene), vagus, cervical cord
    ([(14, ".", "."), (16, ":", "P"), (17, "|", "V"), (19, "|", "M")], ":", "M"),
    # shoulders: brachial plexus (C5-T1) towards the axilla
    ([(5, ".-'''", "."), (10, "__.==-", "X"), (16, ":", "P"), (17, "|", "V"),
      (19, "|", "M")], ":", "M"),
    ([(4, ".", "."), (7, "/=<<'", "X"), (16, ":", "P"), (17, "|", "V"),
      (19, "|", "M")], ":", "M"),
    # arm: musculocutaneous, radial, median, ulnar + thorax: intercostals
    ([(4, ".", "."), (6, "/|||", "KRDU"), (11, ".", "."), (13, "~~~", "I"),
      (16, ":", "P"), (17, "|", "V"), (19, "|", "M")], ":", "M"),
    ([(4, ".", "."), (6, "||||", "KRDU"), (11, ".", "."), (13, "~~~", "I"),
      (16, ":", "P"), (17, "|", "V"), (19, "|", "M")], ":", "M"),
    ([(4, ".", "."), (6, "||||", "KRDU"), (11, ".", "."), (13, "~~~", "I"),
      (16, ":", "P"), (17, "|", "V"), (19, "|", "M")], ":", "M"),
    ([(4, ".", "."), (6, "||||", "KRDU"), (11, ".", "."), (13, "~~~", "I"),
      (16, ":", "P"), (17, "|", "V"), (19, "|", "M")], ":", "M"),
    ([(4, ".", "."), (6, "||||", "KRDU"), (11, ".", "."), (13, "~~~", "I"),
      (16, ":", "P"), (17, "|", "V"), (19, "|", "M")], ":", "M"),
    # elbow: ulnar behind the medial epicondyle; phrenic reaches the diaphragm
    ([(4, ".", "."), (5, "//| \\", "KRDDU"), (11, ".", "."), (13, "~~", "I"),
      (15, "_/", "P"), (17, "|", "V"), (19, "|", "M")], ":", "M"),
    # forearm
    ([(4, ".", "."), (5, "|", "K"), (6, "| | |", "R D U"), (11, ".", "."),
      (17, "*", "V"), (19, "|", "M")], ":", "M"),
    ([(4, ".", "."), (5, "|", "K"), (6, "| | |", "R D U"), (11, ".", "."),
      (19, "|", "M")], ":", "M"),
    # conus medullaris (L1-L2) and lumbar plexus
    ([(4, ".", "."), (5, "|", "K"), (6, "| | |", "R D U"), (11, ".", "."),
      (16, "_/", "F"), (19, "\\", "M")], "V", "M"),
    # cauda equina, femoral nerve, sacral plexus
    ([(4, ".", "."), (6, "| | |", "R D U"), (11, ".", "."), (15, "/", "F"),
      (18, "||", "Q")], "|", "Q"),
    ([(4, ".", "."), (6, "| | |", "R D U"), (11, ".", "."), (14, "/", "F"),
      (17, "/||", "SQQ")], "|", "Q"),
    ([(4, ".", "."), (6, "| | |", "R D U"), (11, ".", "."), (14, "|", "F"),
      (17, "|", "S"), (18, "\\|", "QQ")], "|", "Q"),
    # hands + thighs: femoral fans out, sciatic in the back of the thigh
    ([(4, "(", "."), (5, "\\|||'", "RDDUU"), (10, ".", "."), (12, ".", "."),
      (13, "/|\\", "F"), (17, "|", "S"), (19, ".", ".")], " ", " "),
    ([(4, "(", "."), (5, "/||||", "RDDUU"), (10, ")", "."), (12, ".", "."),
      (13, "' '", "F"), (17, "|", "S"), (19, ".", ".")], " ", " "),
    ([(5, "'''''", "."), (12, ".", "."), (17, "|", "S"), (19, ".", ".")], " ", " "),
    ([(12, ".", "."), (17, "|", "S"), (19, ".", ".")], " ", " "),
    ([(12, ".", "."), (17, "|", "S"), (19, ".", ".")], " ", " "),
    ([(12, ".", "."), (17, "|", "S"), (19, ".", ".")], " ", " "),
    # popliteal fossa: sciatic divides
    ([(12, ".", "."), (16, "/|", "GN"), (19, ".", ".")], " ", " "),
    # fibular neck
    ([(12, ".", "."), (14, "(/", "GG"), (17, "|", "N"), (19, ".", ".")], " ", " "),
    # leg: deep/superficial fibular laterally, tibial posteriorly
    ([(12, ".", "."), (14, "|", "G"), (17, "|", "N"), (19, ".", ".")], " ", " "),
    ([(12, ".", "."), (14, "|", "G"), (17, "|", "N"), (19, ".", ".")], " ", " "),
    ([(12, ".", "."), (14, "|", "G"), (17, "|", "N"), (19, ".", ".")], " ", " "),
    ([(12, ".", "."), (14, "\\", "G"), (17, "|", "N"), (19, ".", ".")], " ", " "),
    # feet: dorsum (fibular) and sole (plantar nerves from the tibial)
    ([(12, "(", "."), (13, "_\\", "GG"), (15, "_", "."), (16, "/\\", "N"), (18, ")", ".")],
     " ", " "),
]


ART, MASK = build_mirrored(_ROWS, HALF_WIDTH)
