"""The termanat Textual application."""

from __future__ import annotations

import random

from rich.console import Group, RenderableType
from rich.table import Table
from rich.text import Text
from textual import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.message import Message
from textual.reactive import reactive
from textual.widgets import (
    Button,
    Header,
    OptionList,
    Static,
    TabbedContent,
    TabPane,
)
from textual.widgets.option_list import Option

from . import __version__
from .bones import BONES, BY_KEY, Bone
from .i18n import LANGUAGES, STRINGS, detect_language
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


def describe(bone: Bone, lang: str) -> Group:
    """The info panel for a bone, in the given language."""
    t = STRINGS[lang]
    info = bone.text(lang)
    head = Text()
    head.append(f"{info.name}\n", "bold #ffb000")
    head.append(f"{t['latin']}: ", "bold")
    head.append(f"{bone.latin}\n", "italic")
    if info.old_names:
        head.append(f"{t['old_names']}: ", "bold")
        head.append(", ".join(info.old_names) + "\n")
    for label, value in (
        ("kind", info.kind),
        ("region", info.region),
        ("count", info.count),
    ):
        head.append(f"{t[label]}: ", "bold")
        head.append(f"{value}\n")
    head.append(f"\n{info.description}")
    parts: list[RenderableType] = [head]
    for label, items in (
        ("landmarks", info.landmarks),
        ("joints", info.joints),
        ("clinical", info.clinical),
    ):
        parts.append(Text(f"\n{t[label]}", "bold #87d787"))
        bullets = Table.grid(padding=(0, 1))
        bullets.add_column(width=3, justify="right")
        bullets.add_column(ratio=1)
        for item in items:
            bullets.add_row("•", item)
        parts.append(bullets)
    fact = Text()
    fact.append(f"\n{t['fact']} ", "bold #5fafff")
    fact.append(info.fact)
    parts.append(fact)
    return Group(*parts)


class ExplorePane(TabPane):
    current_info: RenderableType = ""

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield SkeletonView(id="explore-skeleton")
            with Vertical(classes="side"):
                yield OptionList(
                    *[Option(b.name(self.app.lang), id=b.key) for b in BONES],
                    id="bone-list",
                )
                with VerticalScroll(id="info-scroll"):
                    yield Static(id="info")

    def on_mount(self) -> None:
        self.select(BONES[0].key)

    def apply_language(self) -> None:
        lang = self.app.lang
        options = self.query_one(OptionList)
        current = options.highlighted
        for bone in BONES:
            options.replace_option_prompt(bone.key, bone.name(lang))
        options.highlighted = current
        if key := self.query_one(SkeletonView).highlight:
            self._show_info(key)

    def select(self, key: str) -> None:
        self.query_one(SkeletonView).highlight = key
        self._show_info(key)
        options = self.query_one(OptionList)
        index = options.get_option_index(key)
        if options.highlighted != index:
            options.highlighted = index

    def _show_info(self, key: str) -> None:
        self.current_info = describe(BY_KEY[key], self.app.lang)
        self.query_one("#info", Static).update(self.current_info)
        self.query_one("#info-scroll").scroll_home(animate=False)

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
        self.picked: int | None = None
        self.score = 0
        self.total = 0

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield SkeletonView(style=QUIZ_STYLE, id="quiz-skeleton")
            with Vertical(classes="side"):
                yield Static("", id="question")
                for i in range(self.N_CHOICES):
                    yield Button("", id=f"choice-{i}", classes="choice")
                yield Static("", id="feedback")
                yield Static("", id="score")
                yield Static("", id="quiz-help")

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
        self.picked = None
        self.query_one(SkeletonView).highlight = self.answer.key
        for i in range(len(self.choices)):
            button = self.query_one(f"#choice-{i}", Button)
            button.variant = "default"
            button.disabled = False
        self.apply_language()

    def apply_language(self) -> None:
        t = STRINGS[self.app.lang]
        self.query_one("#question", Static).update(t["question"])
        self.query_one("#quiz-help", Static).update(t["quiz_help"])
        for i, bone in enumerate(self.choices):
            self.query_one(f"#choice-{i}", Button).label = (
                f"{i + 1}. {bone.name(self.app.lang)}"
            )
        self._update_feedback()
        self._update_score()

    def choose(self, index: int) -> None:
        if self.answered or not 0 <= index < len(self.choices):
            return
        assert self.answer is not None
        self.answered = True
        self.total += 1
        self.picked = index
        if self.choices[index] is self.answer:
            self.score += 1
        for i, bone in enumerate(self.choices):
            button = self.query_one(f"#choice-{i}", Button)
            if bone is self.answer:
                button.variant = "success"
            elif i == index:
                button.variant = "error"
            button.disabled = True
        self._update_feedback()
        self._update_score()

    def _update_feedback(self) -> None:
        feedback = Text()
        if self.answered and self.answer is not None and self.picked is not None:
            t = STRINGS[self.app.lang]
            if self.choices[self.picked] is self.answer:
                feedback.append(t["correct"], "bold green")
            else:
                feedback.append(t["wrong"], "bold red")
                feedback.append(t["it_was"])
                feedback.append(self.answer.name(self.app.lang), "bold")
                feedback.append(" ")
            feedback.append(f"({self.answer.latin})", "italic")
        self.query_one("#feedback", Static).update(feedback)

    def _update_score(self) -> None:
        t = STRINGS[self.app.lang]
        self.query_one("#score", Static).update(
            f"{t['score']}: {self.score} / {self.total}"
        )

    @on(Button.Pressed, ".choice")
    def _on_button(self, event: Button.Pressed) -> None:
        assert event.button.id is not None
        self.choose(int(event.button.id.rsplit("-", 1)[1]))


class TermanatApp(App):
    TITLE = "termanat"

    CSS = """
    .side {
        padding: 1 2;
        width: 1fr;
        min-width: 30;
    }
    #bone-list {
        height: 12;
    }
    #info-scroll {
        height: 1fr;
        margin-top: 1;
    }
    #info {
        padding-right: 2;
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
    #keys {
        dock: bottom;
        height: 1;
        padding: 0 1;
        background: $panel;
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
        Binding("n", "next_question", priority=True),
        Binding("enter", "next_question", priority=True),
        Binding("l", "toggle_language", priority=True),
    ]

    def __init__(self, seed: int | None = None, lang: str | None = None) -> None:
        super().__init__()
        self.rng = random.Random(seed)
        self.lang = lang if lang in LANGUAGES else detect_language()

    def compose(self) -> ComposeResult:
        t = STRINGS[self.lang]
        yield Header()
        with TabbedContent(initial="explore"):
            yield ExplorePane(t["tab_explore"], id="explore")
            yield QuizPane(t["tab_quiz"], id="quiz", rng=self.rng)
        yield Static(id="keys")

    def on_mount(self) -> None:
        self.sub_title = STRINGS[self.lang]["subtitle"]
        self._update_keys()
        self.query_one("#bone-list", OptionList).focus()

    def _update_keys(self) -> None:
        """Our own translated key bar (Textual's footer cannot be translated live)."""
        t = STRINGS[self.lang]
        keys = [("q", "key_quit"), ("e", "key_explore"), ("t", "key_quiz")]
        quiz = self._quiz_active()
        if quiz and quiz.answered:
            keys.append(("n", "key_next"))
        keys.append(("l", "key_lang"))
        bar = Text()
        for key, label in keys:
            bar.append(f" {key} ", "bold reverse")
            bar.append(f" {t[label]}   ")
        self.query_one("#keys", Static).update(bar)

    def action_toggle_language(self) -> None:
        self.set_language("fr" if self.lang == "en" else "en")

    def set_language(self, lang: str) -> None:
        self.lang = lang
        t = STRINGS[lang]
        self.sub_title = t["subtitle"]
        tabs = self.query_one(TabbedContent)
        tabs.get_tab("explore").label = t["tab_explore"]
        tabs.get_tab("quiz").label = t["tab_quiz"]
        self.query_one(ExplorePane).apply_language()
        self.query_one(QuizPane).apply_language()
        self._update_keys()

    def action_show_tab(self, tab: str) -> None:
        self.query_one(TabbedContent).active = tab
        self._update_keys()
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

    @on(TabbedContent.TabActivated)
    def _on_tab_activated(self) -> None:
        self._update_keys()

    def _quiz_active(self) -> QuizPane | None:
        if self.query_one(TabbedContent).active == "quiz":
            return self.query_one(QuizPane)
        return None

    def action_answer(self, index: int) -> None:
        if quiz := self._quiz_active():
            quiz.choose(index)
            self._update_keys()

    def action_next_question(self) -> None:
        quiz = self._quiz_active()
        if quiz and quiz.answered:
            quiz.new_question()
            self._update_keys()


def main(argv: list[str] | None = None) -> None:
    import argparse

    parser = argparse.ArgumentParser(
        prog="termanat", description="Discover and learn anatomy inside your terminal."
    )
    parser.add_argument(
        "--lang",
        choices=LANGUAGES,
        help="interface language (default: from your system locale, else English)",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    args = parser.parse_args(argv)
    TermanatApp(lang=args.lang).run()
