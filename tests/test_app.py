import asyncio

from textual.widgets import Button, OptionList, Static, TabbedContent

from termanat.app import ExplorePane, QuizPane, SkeletonView, TermanatApp, main
from termanat.bones import BONES, BY_KEY
from termanat.skeleton import MASK


def run(coro_fn):
    async def go():
        app = TermanatApp(seed=1)
        async with app.run_test(size=(110, 45)) as pilot:
            await coro_fn(app, pilot)

    asyncio.run(go())


def test_explore_starts_on_first_bone():
    async def check(app, pilot):
        view = app.query_one("#explore-skeleton", SkeletonView)
        assert view.highlight == BONES[0].key
        info = str(app.query_one("#info", Static).render())
        assert BONES[0].latin in info

    run(check)


def test_arrow_keys_change_bone():
    async def check(app, pilot):
        app.query_one(OptionList).focus()
        await pilot.press("down")
        await pilot.pause()
        assert app.query_one("#explore-skeleton", SkeletonView).highlight == BONES[1].key

    run(check)


def test_clicking_a_bone_selects_it():
    async def check(app, pilot):
        view = app.query_one("#explore-skeleton", SkeletonView)
        row = next(i for i, m in enumerate(MASK) if "K" in m)
        col = MASK[row].index("K")
        # padding is 1 row / 2 columns
        await pilot.click(view, offset=(col + 2, row + 1))
        await pilot.pause()
        assert view.highlight == "K"
        assert "Patella" in str(app.query_one("#info", Static).render())

    run(check)


def test_quiz_flow():
    async def check(app, pilot):
        await pilot.press("t")
        await pilot.pause()
        assert app.query_one(TabbedContent).active == "quiz"
        quiz = app.query_one(QuizPane)
        assert quiz.query_one(SkeletonView).highlight == quiz.answer.key
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
        assert quiz.answer.name.lower() in str(quiz.query_one("#feedback", Static).render())

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
    assert "termanat 0.1.0" in capsys.readouterr().out


def test_tab_keys_work_while_list_is_focused():
    async def check(app, pilot):
        assert app.focused is app.query_one("#bone-list", OptionList)
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
