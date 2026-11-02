import asyncio
import io

from rich.console import Console

from textual.widgets import Button, OptionList, Static, TabbedContent

from termanat.app import ExplorePane, FigureView, QuizPane, TermanatApp, main
from termanat.systems import BY_ID, SYSTEMS

SKELETON = BY_ID["skeleton"]
BONES = SKELETON.structures
MASK = SKELETON.mask


def info_text(app):
    """The explore info panel as plain text."""
    console = Console(width=200, file=io.StringIO(), color_system=None)
    console.print(app.query_one(ExplorePane).current_info)
    return console.file.getvalue()


def run(coro_fn, lang="en"):
    async def go():
        app = TermanatApp(seed=1, lang=lang, system="skeleton")
        async with app.run_test(size=(110, 45)) as pilot:
            await coro_fn(app, pilot)

    asyncio.run(go())


def test_explore_starts_on_first_bone():
    async def check(app, pilot):
        view = app.query_one("#explore-figure", FigureView)
        assert view.highlight == BONES[0].key
        info = info_text(app)
        assert BONES[0].latin in info
        assert "Landmarks" in info and "Clinical notes" in info

    run(check)


def test_arrow_keys_change_bone():
    async def check(app, pilot):
        app.query_one(OptionList).focus()
        await pilot.press("down")
        await pilot.pause()
        assert app.query_one("#explore-figure", FigureView).highlight == BONES[1].key

    run(check)


def test_clicking_a_bone_selects_it():
    async def check(app, pilot):
        view = app.query_one("#explore-figure", FigureView)
        row = next(i for i, m in enumerate(MASK) if "K" in m)
        col = MASK[row].index("K")
        # padding is 1 row / 2 columns
        await pilot.click(view, offset=(col + 2, row + 1))
        await pilot.pause()
        assert view.highlight == "K"
        assert "Patella" in info_text(app)

    run(check)


def test_quiz_flow():
    async def check(app, pilot):
        await pilot.press("t")
        await pilot.pause()
        assert app.query_one(TabbedContent).active == "quiz"
        quiz = app.query_one(QuizPane)
        assert quiz.query_one(FigureView).highlight == quiz.answer.key
        assert quiz.answer in quiz.choices and len(set(b.key for b in quiz.choices)) == 4

        right = quiz.choices.index(quiz.answer)
        await pilot.press(str(right + 1))
        await pilot.pause()
        assert (quiz.score, quiz.total) == (1, 1)
        assert quiz.query_one(f"#choice-{right}", Button).variant == "success"

        await pilot.press("1")  # ignored: already answered
        assert quiz.total == 1

        first = quiz.answer
        await pilot.press("n")
        await pilot.pause()
        assert not quiz.answered and quiz.answer is not first

        wrong = next(i for i, b in enumerate(quiz.choices) if b is not quiz.answer)
        await pilot.press(str(wrong + 1))
        await pilot.pause()
        assert (quiz.score, quiz.total) == (1, 2)
        assert quiz.query_one(f"#choice-{wrong}", Button).variant == "error"
        assert quiz.answer.name("en") in str(quiz.query_one("#feedback", Static).render())

    run(check)


def test_answer_keys_do_nothing_in_explore():
    async def check(app, pilot):
        await pilot.press("1")
        assert app.query_one(QuizPane).total == 0

    run(check)


def test_version_flag(capsys):
    import pytest

    with pytest.raises(SystemExit):
        main(["--version"])
    assert "termanat 0.2.0" in capsys.readouterr().out


def test_tab_keys_work_while_list_is_focused():
    async def check(app, pilot):
        assert app.focused is app.query_one("#structure-list", OptionList)
        await pilot.press("t")
        await pilot.pause()
        assert app.query_one(TabbedContent).active == "quiz"
        await pilot.press("e")
        await pilot.pause()
        assert app.query_one(TabbedContent).active == "explore"

    run(check)


def test_enter_goes_to_next_question():
    async def check(app, pilot):
        await pilot.press("t", "1")
        await pilot.pause()
        quiz = app.query_one(QuizPane)
        assert quiz.answered
        await pilot.press("enter")
        await pilot.pause()
        assert not quiz.answered

    run(check)


def test_french_interface():
    async def check(app, pilot):
        info = info_text(app)
        assert "Crâne" in info and "Repères anatomiques" in info
        assert app.query_one(OptionList).get_option("I").prompt == "Fibula"
        assert "Quitter" in str(app.query_one("#keys", Static).render())

    run(check, lang="fr")


def test_language_toggle_updates_everything():
    async def check(app, pilot):
        app.query_one(OptionList).focus()
        await pilot.press("down")  # Mandible
        await pilot.press("t", "1")
        await pilot.pause()
        quiz = app.query_one(QuizPane)
        answer = quiz.answer

        await pilot.press("l")
        await pilot.pause()
        assert app.lang == "fr"
        assert app.query_one(TabbedContent).get_tab("explore").label.plain == "Explorer"
        assert "surbrillance" in str(quiz.query_one("#question", Static).render())
        label = str(quiz.query_one("#choice-0", Button).label)
        assert quiz.choices[0].name("fr") in label
        assert answer.name("fr") in str(quiz.query_one("#feedback", Static).render()) or (
            "Bonne réponse" in str(quiz.query_one("#feedback", Static).render())
        )
        info = info_text(app)
        assert "Mandibule" in info
        assert app.query_one(OptionList).highlighted == 1

        await pilot.press("l")
        await pilot.pause()
        assert app.lang == "en"
        assert "Mandible" in info_text(app)

    run(check)


def test_switching_systems():
    async def check(app, pilot):
        figure = app.query_one("#explore-figure", FigureView)
        options = app.query_one(OptionList)
        for system in SYSTEMS[1:] + SYSTEMS[:1]:
            await pilot.press("s")
            await pilot.pause()
            assert app.system is system
            assert figure.system is system
            assert figure.highlight == system.structures[0].key
            assert options.option_count == len(system.structures)
            assert system.structures[0].name("en") in info_text(app)
            quiz = app.query_one(QuizPane)
            assert quiz.answer in system.structures
            assert app.query_one("#quiz-figure", FigureView).system is system

    run(check)


def test_clicking_a_system_tab():
    async def check(app, pilot):
        last = SYSTEMS[-1]
        await pilot.click(f"#systems #{last.id}")
        await pilot.pause()
        assert app.system is last
        assert app.query_one(TabbedContent).active == "explore"

    run(check)


def test_system_names_are_translated():
    async def check(app, pilot):
        await pilot.press("l")
        await pilot.pause()
        tab = app.query_one("#systems #skeleton")
        assert tab.label.plain == "Squelette"

    run(check)


def test_every_structure_renders_in_both_languages():
    from termanat.app import describe

    console = Console(width=80, file=io.StringIO(), color_system=None)
    for system in SYSTEMS:
        for structure in system.structures:
            for lang in ("en", "fr"):
                console.print(describe(structure, lang))
    assert console.file.getvalue()
