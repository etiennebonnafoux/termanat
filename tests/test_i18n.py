import pytest

from termanat.i18n import LANGUAGES, STRINGS, detect_language
from termanat.model import SECTION_KEYS


def test_every_section_has_a_title():
    for lang in LANGUAGES:
        for key in SECTION_KEYS:
            assert STRINGS[lang]["section_" + key]


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
