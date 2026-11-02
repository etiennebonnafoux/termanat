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
    Tab,
    TabbedContent,
    TabPane,
    Tabs,
)
from textual.widgets.option_list import Option

from . import __version__
from .i18n import LANGUAGES, STRINGS, detect_language
from .model import OUTLINE, Structure, System
from .systems import BY_ID, SYSTEMS

REST_STYLE = "#a8a8a8"
OUTLINE_STYLE = "#585858"
HIGHLIGHT_STYLE = "bold #ffb000"
QUIZ_STYLE = "bold #ff5f87"

VIEW_WIDTH = max(s.width for s in SYSTEMS)
VIEW_HEIGHT = max(s.height for s in SYSTEMS)


def render_figure(system: System, highlight: str | None, style: str = HIGHLIGHT_STYLE) -> Text:
    """Render a system's figure as Rich text, with one structure highlighted."""
    text = Text(no_wrap=True)
    for row, (line, mask) in enumerate(zip(system.art, system.mask)):
        for ch, key in zip(line, mask):
            if ch == " ":
                text.append(ch)
            elif key == OUTLINE:
                text.append(ch, OUTLINE_STYLE)
            elif highlight is not None and key == highlight:
                text.append(ch, style)
            else:
                text.append(ch, system.colors.get(key, REST_STYLE))
        if row < len(system.art) - 1:
            text.append("\n")
    return text


class FigureView(Static):
    """The ASCII figure. Clicking a structure posts :class:`FigureView.Clicked`."""

    DEFAULT_CSS = f"""
    FigureView {{
        width: {VIEW_WIDTH + 4};
        height: {VIEW_HEIGHT};
        padding: 0 2;
    }}
    """

    highlight: reactive[str | None] = reactive(None)
    system: reactive[System] = reactive(SYSTEMS[0])

    class Clicked(Message):
        def __init__(self, key: str) -> None:
            super().__init__()
            self.key = key

    def __init__(self, style: str = HIGHLIGHT_STYLE, **kwargs) -> None:
        super().__init__(**kwargs)
        self.highlight_style = style

    def render(self) -> Text:
        return render_figure(self.system, self.highlight, self.highlight_style)

    def on_click(self, event) -> None:
        offset = event.get_content_offset(self)
        if offset is None:
            return
        key = self.system.structure_near(offset.x, offset.y)
        if key:
            self.post_message(self.Clicked(key))


def describe(structure: Structure, lang: str) -> Group:
    """The info panel for a structure, in the given language."""
    t = STRINGS[lang]
    info = structure.text(lang)
    head = Text()
    head.append(f"{info.name}\n", "bold #ffb000")
    head.append(f"{t['latin']}: ", "bold")
    head.append(f"{structure.latin}\n", "italic")
    if info.old_names:
        head.append(f"{t['old_names']}: ", "bold")
        head.append(", ".join(info.old_names) + "\n")
    for label, value in (("kind", info.kind), ("region", info.region), ("count", info.count)):
        if value:
            head.append(f"{t[label]}: ", "bold")
            head.append(f"{value}\n")
    head.append(f"\n{info.description}")
    parts: list[RenderableType] = [head]
    for key, items in info.sections.items():
        parts.append(Text(f"\n{t['section_' + key]}", "bold #87d787"))
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
            yield FigureView(id="explore-figure")
            with Vertical(classes="side"):
                yield OptionList(id="structure-list")
                with VerticalScroll(id="info-scroll"):
                    yield Static(id="info")

    def on_mount(self) -> None:
        self.show_system()

    @property
    def system(self) -> System:
        return self.app.system

    def show_system(self) -> None:
        """Fill the list for the current system and select its first structure."""
        self.query_one(FigureView).system = self.system
        options = self.query_one(OptionList)
        options.clear_options()
        options.add_options(
            [Option(s.name(self.app.lang), id=s.key) for s in self.system.structures]
        )
        self.select(self.system.structures[0].key)

    def apply_language(self) -> None:
        options = self.query_one(OptionList)
        current = options.highlighted
        for s in self.system.structures:
            options.replace_option_prompt(s.key, s.name(self.app.lang))
        options.highlighted = current
        if key := self.query_one(FigureView).highlight:
            self._show_info(key)

    def select(self, key: str) -> None:
        self.query_one(FigureView).highlight = key
        self._show_info(key)
        options = self.query_one(OptionList)
        index = options.get_option_index(key)
        if options.highlighted != index:
            options.highlighted = index

    def _show_info(self, key: str) -> None:
        self.current_info = describe(self.system.by_key[key], self.app.lang)
        self.query_one("#info", Static).update(self.current_info)
        self.query_one("#info-scroll").scroll_home(animate=False)

    @on(OptionList.OptionHighlighted, "#structure-list")
    def _on_highlighted(self, event: OptionList.OptionHighlighted) -> None:
        if event.option.id and event.option.id in self.system.by_key:
            self.select(event.option.id)

    @on(FigureView.Clicked)
    def _on_clicked(self, event: FigureView.Clicked) -> None:
        self.select(event.key)


class QuizPane(TabPane):
    """Shows a highlighted structure and asks for its name."""

    N_CHOICES = 4

    def __init__(self, *args, rng: random.Random, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.rng = rng
        self.answer: Structure | None = None
        self.choices: list[Structure] = []
        self.answered = False
        self.picked: int | None = None
        self.score = 0
        self.total = 0

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield FigureView(style=QUIZ_STYLE, id="quiz-figure")
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
        system: System = self.app.system
        structures = system.structures
        previous = self.answer
        pool = [s for s in structures if s is not previous]
        self.answer = self.rng.choice(pool)
        others = self.rng.sample(
            [s for s in structures if s is not self.answer], self.N_CHOICES - 1
        )
        self.choices = others + [self.answer]
        self.rng.shuffle(self.choices)
        self.answered = False
        self.picked = None
        figure = self.query_one(FigureView)
        figure.system = system
        figure.highlight = self.answer.key
        for i in range(len(self.choices)):
            button = self.query_one(f"#choice-{i}", Button)
            button.variant = "default"
            button.disabled = False
        self.apply_language()

    def apply_language(self) -> None:
        t = STRINGS[self.app.lang]
        self.query_one("#question", Static).update(t["question"])
        self.query_one("#quiz-help", Static).update(t["quiz_help"])
        for i, s in enumerate(self.choices):
            self.query_one(f"#choice-{i}", Button).label = f"{i + 1}. {s.name(self.app.lang)}"
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
        for i, s in enumerate(self.choices):
            button = self.query_one(f"#choice-{i}", Button)
            if s is self.answer:
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
        self.query_one("#score", Static).update(f"{t['score']}: {self.score} / {self.total}")

    @on(Button.Pressed, ".choice")
    def _on_button(self, event: Button.Pressed) -> None:
        assert event.button.id is not None
        self.choose(int(event.button.id.rsplit("-", 1)[1]))


class TermanatApp(App):
    TITLE = "termanat"

    CSS = """
    #systems {
        margin: 0 1;
    }
    .side {
        padding: 1 2;
        width: 1fr;
        min-width: 30;
    }
    #structure-list {
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
        Binding("q", "quit", priority=True),
        Binding("e", "show_tab('explore')", priority=True),
        Binding("t", "show_tab('quiz')", priority=True),
        Binding("s", "next_system", priority=True),
        Binding("1", "answer(0)", priority=True),
        Binding("2", "answer(1)", priority=True),
        Binding("3", "answer(2)", priority=True),
        Binding("4", "answer(3)", priority=True),
        Binding("n", "next_question", priority=True),
        Binding("enter", "next_question", priority=True),
        Binding("l", "toggle_language", priority=True),
    ]

    def __init__(
        self,
        seed: int | None = None,
        lang: str | None = None,
        system: str | None = None,
    ) -> None:
        super().__init__()
        self.rng = random.Random(seed)
        self.lang = lang if lang in LANGUAGES else detect_language()
        self.system: System = BY_ID.get(system or "", SYSTEMS[0])

    def compose(self) -> ComposeResult:
        t = STRINGS[self.lang]
        yield Header()
        yield Tabs(
            *[Tab(s.name(self.lang), id=s.id) for s in SYSTEMS],
            active=self.system.id,
            id="systems",
        )
        with TabbedContent(initial="explore"):
            yield ExplorePane(t["tab_explore"], id="explore")
            yield QuizPane(t["tab_quiz"], id="quiz", rng=self.rng)
        yield Static(id="keys")

    def on_mount(self) -> None:
        self.sub_title = STRINGS[self.lang]["subtitle"]
        self._update_keys()
        self.query_one("#structure-list", OptionList).focus()

    # -- systems ---------------------------------------------------------

    def set_system(self, system_id: str) -> None:
        if system_id == self.system.id:
            return
        self.system = BY_ID[system_id]
        tabs = self.query_one("#systems", Tabs)
        if tabs.active != system_id:
            tabs.active = system_id
        self.query_one(ExplorePane).show_system()
        self.query_one(QuizPane).new_question()
        self._update_keys()

    def action_next_system(self) -> None:
        index = SYSTEMS.index(self.system)
        self.set_system(SYSTEMS[(index + 1) % len(SYSTEMS)].id)

    @on(Tabs.TabActivated, "#systems")
    def _on_system_tab(self, event: Tabs.TabActivated) -> None:
        event.stop()  # do not let TabbedContent see it
        if event.tab.id:
            self.set_system(event.tab.id)

    # -- language --------------------------------------------------------

    def action_toggle_language(self) -> None:
        self.set_language("fr" if self.lang == "en" else "en")

    def set_language(self, lang: str) -> None:
        self.lang = lang
        t = STRINGS[lang]
        self.sub_title = t["subtitle"]
        tabs = self.query_one(TabbedContent)
        tabs.get_tab("explore").label = t["tab_explore"]
        tabs.get_tab("quiz").label = t["tab_quiz"]
        systems = self.query_one("#systems", Tabs)
        for s in SYSTEMS:
            systems.query_one(f"#{s.id}", Tab).label = s.name(lang)
        self.query_one(ExplorePane).apply_language()
        self.query_one(QuizPane).apply_language()
        self._update_keys()

    # -- key bar ---------------------------------------------------------

    def _update_keys(self) -> None:
        """Our own translated key bar (Textual's footer cannot be translated live)."""
        t = STRINGS[self.lang]
        keys = [("q", "key_quit"), ("e", "key_explore"), ("t", "key_quiz"), ("s", "key_system")]
        quiz = self._quiz_active()
        if quiz and quiz.answered:
            keys.append(("n", "key_next"))
        keys.append(("l", "key_lang"))
        bar = Text()
        for key, label in keys:
            bar.append(f" {key} ", "bold reverse")
            bar.append(f" {t[label]}   ")
        self.query_one("#keys", Static).update(bar)

    # -- tabs and quiz -----------------------------------------------------

    def action_show_tab(self, tab: str) -> None:
        self.query_one(TabbedContent).active = tab
        self._update_keys()
        if tab == "explore":
            self.query_one("#structure-list", OptionList).focus()
        else:
            self.set_focus(None)

    @on(TabbedContent.TabActivated)
    def _on_tab_activated(self) -> None:
        self._update_keys()

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
    parser.add_argument(
        "--system",
        choices=[s.id for s in SYSTEMS],
        default=SYSTEMS[0].id,
        help="body system to open first (default: %(default)s)",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    args = parser.parse_args(argv)
    TermanatApp(lang=args.lang, system=args.system).run()
