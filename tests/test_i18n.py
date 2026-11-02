from dataclasses import fields

import pytest

from termanat.bones import BONES, BoneText
from termanat.i18n import LANGUAGES, STRINGS, detect_language


def test_every_bone_is_translated_in_every_language():
    for bone in BONES:
        assert set(bone.texts) == set(LANGUAGES)
        for lang in LANGUAGES:
            text = bone.text(lang)
            for f in fields(BoneText):
                if f.name == "old_names":
                    continue
                assert getattr(text, f.name), (bone.key, lang, f.name)


def test_translations_have_the_same_number_of_items():
    for bone in BONES:
        en, fr = bone.text("en"), bone.text("fr")
        for name in ("landmarks", "joints", "clinical"):
            assert len(getattr(en, name)) == len(getattr(fr, name)), (bone.key, name)


def test_names_are_unique_per_language():
    for lang in LANGUAGES:
        names = [b.name(lang) for b in BONES]
        assert len(names) == len(set(names))


def test_interface_strings_have_the_same_keys():
    assert set(STRINGS["en"]) == set(STRINGS["fr"])


@pytest.mark.parametrize(
    "env, expected",
    [
        ({}, "en"),
        ({"LANG": "fr_FR.UTF-8"}, "fr"),
        ({"LANG": "en_US.UTF-8"}, "en"),
        ({"LANG": "de_DE.UTF-8"}, "en"),
        ({"LANG": "C.UTF-8"}, "en"),
        ({"LC_ALL": "fr_CA.UTF-8", "LANG": "en_US.UTF-8"}, "fr"),
        ({"LANGUAGE": "fr:en", "LANG": "en_US.UTF-8"}, "fr"),
        ({"LANGUAGE": "", "LANG": "fr_BE.UTF-8"}, "fr"),
    ],
)
def test_detect_language(env, expected):
    assert detect_language(env) == expected
