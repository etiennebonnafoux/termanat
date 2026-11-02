"""Data model shared by every body system (skeleton, muscles, organs...).

A *system* is one ASCII figure plus the anatomical structures drawn on it.

The figure is two lists of strings of identical shape:

* ``art``: what is drawn;
* ``mask``: for each character of ``art``, the key of the structure it belongs
  to. A space means "nothing here" and must match a space in ``art``.
  ``OUTLINE`` (``.``) marks decoration such as a body silhouette: it is drawn
  dimmed and is not clickable.

Each structure has a one-character key used in the mask, a Latin name, and one
:class:`StructureText` per language.
"""

from __future__ import annotations

from dataclasses import dataclass, field

OUTLINE = "."

#: Section keys a structure may use, in display order. Their titles are in
#: ``i18n.STRINGS`` under ``section_<key>``.
SECTION_KEYS = (
    "parts",
    "landmarks",
    "joints",
    "insertions",
    "action",
    "course",
    "branches",
    "territory",
    "relations",
    "function",
    "vascularisation",
    "innervation",
    "clinical",
)

MAX_WIDTH = 45
MAX_HEIGHT = 38
MIN_STRUCTURES = 6


@dataclass(frozen=True)
class StructureText:
    """Everything about a structure that depends on the language."""

    name: str
    kind: str  # e.g. "Long bone", "Hollow organ", "Skeletal muscle", "Elastic artery"
    region: str
    description: str
    sections: dict[str, list[str]]  # keys from SECTION_KEYS
    fact: str
    count: str = ""  # optional, e.g. "2" or "24 (12 pairs)"
    old_names: list[str] = field(default_factory=list)  # former nomenclature


@dataclass(frozen=True)
class Structure:
    key: str  # one character used in the mask
    latin: str  # Terminologia Anatomica
    texts: dict[str, StructureText]

    def text(self, lang: str) -> StructureText:
        return self.texts[lang]

    def name(self, lang: str) -> str:
        return self.texts[lang].name


@dataclass(frozen=True)
class System:
    id: str
    names: dict[str, str]  # per language, e.g. {"en": "Skeleton", "fr": "Squelette"}
    art: list[str]
    mask: list[str]
    structures: list[Structure]  # display order
    #: optional resting colour per structure key (e.g. arteries red, veins blue)
    colors: dict[str, str] = field(default_factory=dict)

    @property
    def width(self) -> int:
        return max(len(line) for line in self.art)

    @property
    def height(self) -> int:
        return len(self.art)

    @property
    def by_key(self) -> dict[str, Structure]:
        return {s.key: s for s in self.structures}

    def name(self, lang: str) -> str:
        return self.names[lang]

    def structure_at(self, x: int, y: int) -> str | None:
        """Key of the structure drawn at column ``x``, row ``y`` (or ``None``)."""
        if 0 <= y < len(self.mask) and 0 <= x < len(self.mask[y]):
            key = self.mask[y][x]
            if key not in (" ", OUTLINE):
                return key
        return None

    def structure_near(self, x: int, y: int) -> str | None:
        """Like :meth:`structure_at`, tolerant of clicks on gaps inside a shape."""
        for dx in (0, -1, 1, -2, 2):
            key = self.structure_at(x + dx, y)
            if key:
                return key
        return None


def build_mirrored(
    rows: list[tuple[list[tuple[int, str, str]], str, str]], half_width: int
) -> tuple[list[str], list[str]]:
    """Build a left/right symmetric figure from its left half.

    Each row is ``(segments, center_char, center_mask)`` where a segment is
    ``(column, text, mask)``; ``mask`` is a single key for the whole text or one
    key per character. The right half is the mirror image of the left half.
    """
    mirror = str.maketrans("/\\()<>[]{}", "\\/)(><][}{")
    art: list[str] = []
    mask: list[str] = []
    for segments, center, center_mask in rows:
        a = [" "] * half_width
        m = [" "] * half_width
        for col, text, mk in segments:
            if len(mk) == 1:
                mk = mk * len(text)
            if len(mk) != len(text) or col + len(text) > half_width:
                raise ValueError(f"bad segment {text!r} at column {col}")
            for i, (ch, key) in enumerate(zip(text, mk)):
                if a[col + i] != " ":
                    raise ValueError(f"overlapping segment {text!r} at column {col}")
                a[col + i] = ch
                m[col + i] = key if ch != " " else " "
        left, left_mask = "".join(a), "".join(m)
        art.append(left + center + left[::-1].translate(mirror))
        mask.append(left_mask + (center_mask if center != " " else " ") + left_mask[::-1])
    return art, mask


def validate_system(system: System, languages: tuple[str, ...] = ("en", "fr")) -> None:
    """Raise ``AssertionError`` with a helpful message if ``system`` is malformed."""
    sid = system.id
    assert system.art and len(system.art) == len(system.mask), f"{sid}: art/mask rows differ"
    assert system.height <= MAX_HEIGHT, f"{sid}: {system.height} rows > {MAX_HEIGHT}"
    assert system.width <= MAX_WIDTH, f"{sid}: {system.width} columns > {MAX_WIDTH}"
    for y, (line, mask) in enumerate(zip(system.art, system.mask)):
        assert len(line) == len(mask), f"{sid}: row {y} art and mask lengths differ"
        for x, (ch, key) in enumerate(zip(line, mask)):
            assert (ch == " ") == (key == " "), (
                f"{sid}: row {y} col {x}: art {ch!r} vs mask {key!r} "
                "(a space in one must be a space in the other)"
            )
    keys = [s.key for s in system.structures]
    assert len(keys) == len(set(keys)), f"{sid}: duplicate structure keys"
    assert all(len(k) == 1 and k not in (" ", OUTLINE) for k in keys), f"{sid}: bad key"
    assert len(keys) >= MIN_STRUCTURES, f"{sid}: needs at least {MIN_STRUCTURES} structures"
    drawn = set("".join(system.mask)) - {" ", OUTLINE}
    assert drawn == set(keys), (
        f"{sid}: drawn but not described: {sorted(drawn - set(keys))}; "
        f"described but not drawn: {sorted(set(keys) - drawn)}"
    )
    assert set(system.names) == set(languages), f"{sid}: system name translations"
    assert set(system.colors) <= set(keys), f"{sid}: colors for unknown keys"
    for lang in languages:
        names = [s.name(lang) for s in system.structures]
        assert len(names) == len(set(names)), f"{sid}/{lang}: duplicate names"
    for s in system.structures:
        assert set(s.texts) == set(languages), f"{sid}/{s.key}: missing translation"
        ref = s.text(languages[0])
        for lang in languages:
            t = s.text(lang)
            where = f"{sid}/{s.key}/{lang}"
            for attr in ("name", "kind", "region", "description", "fact"):
                assert getattr(t, attr).strip(), f"{where}: empty {attr}"
            assert t.sections, f"{where}: no sections"
            assert set(t.sections) <= set(SECTION_KEYS), (
                f"{where}: unknown sections {set(t.sections) - set(SECTION_KEYS)}"
            )
            assert all(t.sections.values()), f"{where}: empty section"
            assert list(t.sections) == list(ref.sections), f"{where}: sections differ from {languages[0]}"
            for k, items in t.sections.items():
                assert len(items) == len(ref.sections[k]), f"{where}: '{k}' item count differs"
            assert bool(t.count) == bool(ref.count), f"{where}: count present in one language only"
