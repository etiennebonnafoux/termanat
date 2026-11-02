"""Interface strings and language selection."""

from __future__ import annotations

import os

LANGUAGES = ("en", "fr")
DEFAULT = "en"

STRINGS: dict[str, dict[str, str]] = {
    "en": {
        "subtitle": "Discover and learn anatomy inside your terminal",
        "tab_explore": "Explore",
        "tab_quiz": "Quiz",
        "latin": "Latin",
        "old_names": "Former names",
        "kind": "Type",
        "region": "Region",
        "count": "Count",
        "section_parts": "Parts",
        "section_landmarks": "Landmarks",
        "section_joints": "Joints",
        "section_insertions": "Attachments (origin → insertion)",
        "section_action": "Action",
        "section_course": "Course",
        "section_branches": "Branches",
        "section_territory": "Territory",
        "section_relations": "Relations",
        "section_function": "Function",
        "section_vascularisation": "Blood supply",
        "section_innervation": "Innervation",
        "section_clinical": "Clinical notes",
        "fact": "Did you know?",
        "question": "What is highlighted?",
        "correct": "Correct! ",
        "wrong": "Not quite. ",
        "it_was": "It was: ",
        "score": "Score",
        "quiz_help": "Press 1-4 or click an answer. Enter or n: next question.",
        "key_quit": "Quit",
        "key_explore": "Explore",
        "key_quiz": "Quiz",
        "key_next": "Next",
        "key_system": "System",
        "key_lang": "Français",
    },
    "fr": {
        "subtitle": "Découvrez et apprenez l'anatomie dans votre terminal",
        "tab_explore": "Explorer",
        "tab_quiz": "Quiz",
        "latin": "Latin",
        "old_names": "Anciens noms",
        "kind": "Type",
        "region": "Région",
        "count": "Nombre",
        "section_parts": "Constitution",
        "section_landmarks": "Repères anatomiques",
        "section_joints": "Articulations",
        "section_insertions": "Insertions (origine → terminaison)",
        "section_action": "Action",
        "section_course": "Trajet",
        "section_branches": "Branches",
        "section_territory": "Territoire",
        "section_relations": "Rapports",
        "section_function": "Fonction",
        "section_vascularisation": "Vascularisation",
        "section_innervation": "Innervation",
        "section_clinical": "Clinique",
        "fact": "Le saviez-vous ?",
        "question": "Qu'est-ce qui est en surbrillance ?",
        "correct": "Bonne réponse ! ",
        "wrong": "Raté. ",
        "it_was": "C'était : ",
        "score": "Score",
        "quiz_help": "Tapez 1-4 ou cliquez une réponse. Entrée ou n : question suivante.",
        "key_quit": "Quitter",
        "key_explore": "Explorer",
        "key_quiz": "Quiz",
        "key_next": "Suivante",
        "key_system": "Système",
        "key_lang": "English",
    },
}


def detect_language(environ: dict[str, str] | None = None) -> str:
    """Pick the language from the usual locale variables, defaulting to English."""
    env = os.environ if environ is None else environ
    for var in ("LANGUAGE", "LC_ALL", "LC_MESSAGES", "LANG"):
        value = env.get(var, "")
        if not value:
            continue
        # LANGUAGE may hold a priority list such as "fr:en".
        for part in value.split(":"):
            code = part.split("_")[0].split(".")[0].lower()
            if code in LANGUAGES:
                return code
            if code and code not in ("c", "posix"):
                return DEFAULT
    return DEFAULT
