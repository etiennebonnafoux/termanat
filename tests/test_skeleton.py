from termanat.bones import BONES, BY_KEY
from termanat.skeleton import ART, MASK, WIDTH, bone_at, bone_at_or_near


def test_art_and_mask_have_same_shape():
    assert len(ART) == len(MASK)
    for line, mask in zip(ART, MASK):
        assert len(line) == len(mask) == WIDTH


def test_every_drawn_character_belongs_to_a_bone():
    for line, mask in zip(ART, MASK):
        for ch, key in zip(line, mask):
            assert (ch == " ") == (key == " ")


def test_mask_keys_match_bone_data():
    drawn = set("".join(MASK)) - {" "}
    assert drawn == set(BY_KEY)
    assert len(BY_KEY) == len(BONES)


def test_skeleton_is_symmetric():
    for mask in MASK:
        assert mask == mask[::-1]


def test_radius_is_lateral_and_ulna_is_medial():
    row = next(i for i, m in enumerate(MASK) if "D" in m)
    left = MASK[row][: WIDTH // 2]
    assert left.index("D") < left.index("U")


def test_bone_lookup():
    assert bone_at(0, 0) is None
    assert bone_at(WIDTH // 2, 0) == "S"
    assert bone_at(-1, 0) is None
    assert bone_at(0, 999) is None
    row = next(i for i, m in enumerate(MASK) if "F" in m)
    gap = MASK[row].index("F") + 1  # the space inside "| |"
    assert bone_at(gap, row) is None
    assert bone_at_or_near(gap, row) == "F"
