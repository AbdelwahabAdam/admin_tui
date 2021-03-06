#!/usr/bin/env python
"""
Horizontal split example.
"""
from prompt_toolkit.application import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, Window, VSplit, FloatContainer, Float
from prompt_toolkit.layout.controls import FormattedTextControl, BufferControl
from prompt_toolkit.layout.layout import Layout 
from prompt_toolkit.layout import Dimension, HSplit, Layout, ScrollablePane

from prompt_toolkit.buffer import Buffer
from prompt_toolkit.document import Document
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.layout.menus import CompletionsMenu
from prompt_toolkit.shortcuts import input_dialog

from prompt_toolkit.widgets import (
    Box,
    Button,
    Checkbox,
    Dialog,
    Frame,
    Label,
    MenuContainer,
    MenuItem,
    ProgressBar,
    RadioList,
    TextArea,
)
# 1. The layout

top_text = (
    "Hopa example.\n"
    "[ctrl + q] Quit [ctrl + a] Focus left top [ctrl + b] Right top [ctrl + c] Left bottom [ctrl + d] Right bottom."
)


animal_completer = WordCompleter(
    [
        "alligator",
        "ant",
        "ape",
        "bat",
        "bear",
        "beaver",
        "bee",
        "bison",
        "butterfly",
        "cat",
        "chicken",
        "crocodile",
        "dinosaur",
        "dog",
        "dolphin",
        "dove",
        "duck",
        "eagle",
        "elephant",
        "fish",
        "goat",
        "gorilla",
        "kangaroo",
        "leopard",
        "lion",
        "mouse",
        "rabbit",
        "rat",
        "snake",
        "spider",
        "turkey",
        "turtle",
    ],
    ignore_case=True,
)

checkbox1 = Checkbox(text="Checkbox")
checkbox2 = Checkbox(text="Checkbox")

radios = RadioList(
    values=[
        ("Red", "red"),
        ("Green", "green"),
        ("Blue", "blue"),
        ("Orange", "orange"),
        ("Yellow", "yellow"),
        ("Purple", "Purple"),
        ("Brown", "Brown"),
    ]
)

left_top = Frame(Label(text=f"label"), width=Dimension())


left_bottom = Window(BufferControl(Buffer(document=Document('Normal Text '))))


right_top = input_dialog(
    title='Input dialog example',
    text='Please type your name:')


right_bottom = Frame(
    title="Checkbox list",
    body=HSplit([checkbox1, checkbox2]),
)


body = FloatContainer(
    content=HSplit(
        [
            VSplit(
                [
                   VSplit([Label(text='test wig', width=len('title')+1)], height=1),
                   Window(width=6, char=" "),
                   VSplit([Label(text='test wig', width=len('title')+1)], height=1),

                ]
            ),
            Window(height=1, char="-"),  # Horizontal line in the middle.
            VSplit(
                [
                     VSplit([Label(text='test wig', width=len('title')+1)], height=1),
                    Window(width=6, char=" "),
                   VSplit([Label(text='test wig', width=len('title')+1)], height=1),
                ]
            ),

        ]
    ),
    floats=[
        Float(
            xcursor=True,
            ycursor=True,
            content=CompletionsMenu(max_height=16, scroll_offset=1),
        )
    ],
)


# 2. Key bindings
kb = KeyBindings()


@kb.add("c-q")
def _(event):
    "Quit application."
    event.app.exit()


@kb.add("c-a")
def _(event):
    event.app.layout.focus(left_top)


@kb.add("c-b")
def _(event):
    event.app.layout.focus(right_top)


@kb.add("c-c")
def _(event):
    event.app.layout.focus(left_bottom)


@kb.add("c-d")
def _(event):
    event.app.layout.focus(right_bottom)


@kb.add("tab")
def _(event):
    event.app.layout.focus_next()


@kb.add("s-tab")
def _(event):
    event.app.layout.focus_previous()


# 3. The `Application`
application = Application(layout=Layout(
    body), key_bindings=kb, full_screen=True)


def run():
    application.run()


if __name__ == "__main__":
    run()