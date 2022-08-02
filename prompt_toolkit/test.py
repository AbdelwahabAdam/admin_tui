#!/usr/bin/env python
"""
A simple example of a scrollable pane.
"""
from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.layout import Dimension, HSplit, Layout, ScrollablePane
from prompt_toolkit.widgets import Frame, Label, TextArea
from table import *


table = [
    [Label('Cliend ID'), Label('Client Name'), Label(
        'Grant Type'), Label('Access Token')],
    [Label('Cliend ID'), Label('Client Name'), Label(
        'Grant Type'), Label('Access Token')],
    [Label('Cliend ID'), Label('Client Name'), Label(
        'Grant Type'), Label('Access Token')],
    [Label('Cliend ID'), Label('Client Name'), Label(
        'Grant Type'), Label('Access Token')],
]

# # table = TextArea(txt2)

# layout = Layout(
#     Box(
#         Table(
#             table=table,
#             column_width=D.exact(15),
#             column_widths=[None],
#             borders=DoubleBorder),
#         padding=1,
#     ),
# )


def main():
    # Create a big layout of many text areas, then wrap them in a `ScrollablePane`.
    root_container = Frame(
        ScrollablePane(
            HSplit(
                [
                    Table(
                        table=table,
                        column_width=D.exact(15),
                        borders=ThickBorder),
                ]
            )
        )
    )

    layout = Layout(container=root_container)

    # Key bindings.
    kb = KeyBindings()

    @kb.add("c-c")
    def exit(event) -> None:
        get_app().exit()

    kb.add("tab")(focus_next)
    kb.add("s-tab")(focus_previous)

    # Create and run application.
    application = Application(layout=layout, key_bindings=kb, full_screen=True)
    application.run()


if __name__ == "__main__":
    main()
