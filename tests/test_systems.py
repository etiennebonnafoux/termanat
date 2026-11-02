import pytest

from termanat.model import OUTLINE, validate_system
from termanat.systems import BY_ID, SYSTEMS

EXPECTED = ["skeleton", "muscles", "digestive", "circulatory", "nervous"]


def test_all_systems_are_registered_in_order():
    assert [s.id for s in SYSTEMS] == EXPECTED


@pytest.mark.parametrize("system", SYSTEMS, ids=lambda s: s.id)
def test_system_is_valid(system):
    validate_system(system)


@pytest.mark.parametrize("system", SYSTEMS, ids=lambda s: s.id)
def test_every_structure_is_clickable(system):
    for structure in system.structures:
        hits = [
            (x, y)
            for y, row in enumerate(system.mask)
            for x, key in enumerate(row)
            if key == structure.key
        ]
        assert hits, structure.key
        x, y = hits[0]
        assert system.structure_at(x, y) == structure.key


def test_outline_is_not_clickable():
    for system in SYSTEMS:
        for y, row in enumerate(system.mask):
            for x, key in enumerate(row):
                if key == OUTLINE:
                    assert system.structure_at(x, y) is None


# --- skeleton specifics --------------------------------------------------

SKELETON = BY_ID["skeleton"]


def test_skeleton_is_symmetric():
    for mask in SKELETON.mask:
        assert mask == mask[::-1]


def test_radius_is_lateral_and_ulna_is_medial():
    row = next(i for i, m in enumerate(SKELETON.mask) if "D" in m)
    left = SKELETON.mask[row][: SKELETON.width // 2]
    assert left.index("D") < left.index("U")


def test_lookup_near_a_gap():
    mask = SKELETON.mask
    assert SKELETON.structure_at(0, 0) is None
    assert SKELETON.structure_at(SKELETON.width // 2, 0) == "S"
    assert SKELETON.structure_at(-1, 0) is None
    assert SKELETON.structure_at(0, 999) is None
    row = next(i for i, m in enumerate(mask) if "F" in m)
    gap = mask[row].index("F") + 1  # the space inside "| |"
    assert SKELETON.structure_at(gap, row) is None
    assert SKELETON.structure_near(gap, row) == "F"
