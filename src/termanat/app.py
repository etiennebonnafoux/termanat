"""The termanat Textual application."""

from __future__ import annotations

import random

from rich.text import Text
from textual import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.message import Message
from textual.reactive import reactive
from textual.widgets import (
    Button,
    Footer,
    Header,
    OptionList,
    Static,
    TabbedContent,
    TabPane,
)
from textual.widgets.option_list import Option

from . import __version__
from .bones import BONES, BY_KEY, Bone
from .skeleton import ART, HEIGHT, MASK, WIDTH, bone_at_or_near

BONE_STYLE = "#a8a8a8"
HIGHLIGHT_STYLE = "bold #ffb000"
QUIZ_STYLE = "bold #ff5f87"


def render_skeleton(highlight: str | None, style: str = HIGHLIGHT_STYLE) -> Text:
    """Render the skeleton as Rich text, with one bone highlighted."""
    text = Text(no_wrap=True)
    for row, (line, mask) in enumerate(zip(ART, MASK)):
        for ch, key in zip(line, mask):
            if ch == " ":
                text.append(ch)
            elif highlight is not None and key == highlight:
                text.append(ch, style)
            else:
                text.append(ch, BONE_STYLE)
        if row < len(ART) - 1:
            text.append("\n")
    return text


class SkeletonView(Static):
    """The ASCII skeleton. Clicking a bone posts :class:`SkeletonView.Clicked`."""

    DEFAULT_CSS = f"""
    SkeletonView {{
        width: {WIDTH + 4};
        height: {HEIGHT + 2};
        padding: 1 2;
    }}
    """

    highlight: reactive[str | None] = reactive(None)

    class Clicked(Message):
        def __init__(self, key: str) -> None:
            super().__init__()
            self.key = key

    def __init__(self, style: str = HIGHLIGHT_STYLE, **kwargs) -> None:
        super().__init__(**kwargs)
        self.highlight_style = style

    def render(self) -> Text:
        return render_skeleton(self.highlight, self.highlight_style)

    def on_click(self, event) -> None:
        offset = event.get_content_offset(self)
        if offset is None:
            return
        key = bone_at_or_near(offset.x, offset.y)
        if key:
            self.post_message(self.Clicked(key))


def describe(bone: Bone) -> Text:
    text = Text()
    text.append(f"{bone.name}\n", "bold #ffb000")
    text.append(f"{bone.latin}\n\n", "italic")
    text.append("Region: ", "bold")
    text.append(f"{bone.region}\n")
    text.append("Count:  ", "bold")
    text.append(f"{bone.count}\n\n")
    text.append(f"{bone.description}\n\n")
    text.append("Did you know? ", "bold #5fafff")
    text.append(bone.fact)
    return text


class ExplorePane(TabPane):
    def compose(self) -> ComposeResult:
        with Horizontal():
            yield SkeletonView(id="explore-skeleton")
            with Vertical(classes="side"):
                yield OptionList(
                    *[Option(b.name, id=b.key) for b in BONES], id="bone-list"
                )
                with VerticalScroll(id="info-scroll"):
                    yield Static(id="info")

    def on_mount(self) -> None:
        self.select(BONES[0].key)

    def select(self, key: str) -> None:
        self.query_one(SkeletonView).highlight = key
        self.query_one("#info", Static).update(describe(BY_KEY[key]))
        options = self.query_one(OptionList)
        index = options.get_option_index(key)
        if options.highlighted != index:
            options.highlighted = index

    @on(OptionList.OptionHighlighted, "#bone-list")
    def _on_highlighted(self, event: OptionList.OptionHighlighted) -> None:
        if event.option.id:
            self.select(event.option.id)

    @on(SkeletonView.Clicked)
    def _on_clicked(self, event: SkeletonView.Clicked) -> None:
        self.select(event.key)


class QuizPane(TabPane):
    """Shows a highlighted bone and asks for its name."""

    N_CHOICES = 4

    def __init__(self, *args, rng: random.Random, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.rng = rng
        self.answer: Bone | None = None
        self.choices: list[Bone] = []
        self.answered = False
        self.score = 0
        self.total = 0

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield SkeletonView(style=QUIZ_STYLE, id="quiz-skeleton")
            with Vertical(classes="side"):
                yield Static("Which bone is highlighted?", id="question")
                for i in range(self.N_CHOICES):
                    yield Button("", id=f"choice-{i}", classes="choice")
                yield Static("", id="feedback")
                yield Static("", id="score")
                yield Static(
                    "Press 1-4 or click an answer. Enter or n: next question.",
                    id="quiz-help",
                )

    def on_mount(self) -> None:
        self.new_question()

    def new_question(self) -> None:
        previous = self.answer
        pool = [b for b in BONES if b is not previous]
        self.answer = self.rng.choice(pool)
        others = self.rng.sample(
            [b for b in BONES if b is not self.answer], self.N_CHOICES - 1
        )
        self.choices = others + [self.answer]
        self.rng.shuffle(self.choices)
        self.answered = False
        self.query_one(SkeletonView).highlight = self.answer.key
        for i, bone in enumerate(self.choices):
            button = self.query_one(f"#choice-{i}", Button)
            button.label = f"{i + 1}. {bone.name}"
            button.variant = "default"
            button.disabled = False
        self.query_one("#feedback", Static).update("")
        self._update_score()

    def choose(self, index: int) -> None:
        if self.answered or not 0 <= index < len(self.choices):
            return
        assert self.answer is not None
        self.answered = True
        self.total += 1
        picked = self.choices[index]
        correct = picked is self.answer
        if correct:
            self.score += 1
        for i, bone in enumerate(self.choices):
            button = self.query_one(f"#choice-{i}", Button)
            if bone is self.answer:
                button.variant = "success"
            elif i == index:
                button.variant = "error"
            button.disabled = True
        feedback = Text()
        if correct:
            feedback.append("Correct! ", "bold green")
        else:
            feedback.append("Not quite. ", "bold red")
            feedback.append("It was the ")
            feedback.append(self.answer.name.lower(), "bold")
            feedback.append(". ")
        feedback.append(f"({self.answer.latin})", "italic")
        self.query_one("#feedback", Static).update(feedback)
        self._update_score()

    def _update_score(self) -> None:
        self.query_one("#score", Static).update(f"Score: {self.score} / {self.total}")

    @on(Button.Pressed, ".choice")
    def _on_button(self, event: Button.Pressed) -> None:
        assert event.button.id is not None
        self.choose(int(event.button.id.rsplit("-", 1)[1]))


class TermanatApp(App):
    TITLE = "termanat"
    SUB_TITLE = "Discover and learn anatomy inside your terminal"

    CSS = """
    .side {
        padding: 1 2;
        width: 1fr;
        min-width: 30;
    }
    #bone-list {
        height: 1fr;
        min-height: 8;
        max-height: 21;
    }
    #info-scroll {
        height: 1fr;
        margin-top: 1;
    }
    #question {
        text-style: bold;
        margin-bottom: 1;
    }
    .choice {
        width: 100%;
        margin-bottom: 1;
    }
    #feedback, #score {
        margin-bottom: 1;
    }
    #quiz-help {
        color: $text-muted;
    }
    """

    BINDINGS = [
        Binding("q", "quit", "Quit", priority=True),
        Binding("e", "show_tab('explore')", "Explore", priority=True),
        Binding("t", "show_tab('quiz')", "Quiz", priority=True),
        Binding("1", "answer(0)", show=False, priority=True),
        Binding("2", "answer(1)", show=False, priority=True),
        Binding("3", "answer(2)", show=False, priority=True),
        Binding("4", "answer(3)", show=False, priority=True),
        Binding("n", "next_question", "Next", priority=True),
        Binding("enter", "next_question", show=False, priority=True),
    ]

    def __init__(self, seed: int | None = None) -> None:
        super().__init__()
        self.rng = random.Random(seed)

    def compose(self) -> ComposeResult:
        yield Header()
        with TabbedContent(initial="explore"):
            yield ExplorePane("Explore bones", id="explore")
            yield QuizPane("Quiz", id="quiz", rng=self.rng)
        yield Footer()

    def on_mount(self) -> None:
        self.query_one("#bone-list", OptionList).focus()

    def action_show_tab(self, tab: str) -> None:
        self.query_one(TabbedContent).active = tab
        if tab == "explore":
            self.query_one("#bone-list", OptionList).focus()
        else:
            self.set_focus(None)

    def check_action(self, action: str, parameters: tuple[object, ...]) -> bool | None:
        # Quiz keys only exist on the quiz tab; elsewhere the key goes to the
        # focused widget as usual.
        if action == "answer":
            quiz = self._quiz_active()
            return bool(quiz and not quiz.answered)
        if action == "next_question":
            quiz = self._quiz_active()
            return bool(quiz and quiz.answered)
        return True

    def _quiz_active(self) -> QuizPane | None:
        if self.query_one(TabbedContent).active == "quiz":
            return self.query_one(QuizPane)
        return None

    def action_answer(self, index: int) -> None:
        if quiz := self._quiz_active():
            quiz.choose(index)

    def action_next_question(self) -> None:
        quiz = self._quiz_active()
        if quiz and quiz.answered:
            quiz.new_question()


def main(argv: list[str] | None = None) -> None:
    import argparse

    parser = argparse.ArgumentParser(
        prog="termanat", description="Discover and learn anatomy inside your terminal."
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.parse_args(argv)
    TermanatApp().run()
