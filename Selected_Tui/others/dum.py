#!/usr/bin/env python3
"""
"""
import time

from pygments.lexers.html import HtmlLexer
from prompt_toolkit.formatted_text import HTML, merge_formatted_text

from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.layout.containers import Float, HSplit, VSplit, Window
from prompt_toolkit.layout.screen import _CHAR_CACHE, Screen, WritePosition 
from prompt_toolkit.output import ColorDepth, Output

from prompt_toolkit.layout.containers import (
    AnyContainer,
    Dimension,
    Float,
    HSplit,
    VSplit,
    Window,
    WindowAlign,
    DynamicContainer,
    Container,
    MouseHandlers

)
from prompt_toolkit.utils import to_str
from prompt_toolkit.layout.dimension import AnyDimension
from prompt_toolkit.layout.margins import ScrollbarMargin
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.containers import VerticalAlign , HorizontalAlign
from prompt_toolkit.layout.dimension import D
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout.menus import CompletionsMenu
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles import Style
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
    CheckboxList,
)

from typing import (
    TYPE_CHECKING,
    Callable,
    Dict,
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
    cast,
)
from prompt_toolkit.key_binding import KeyBindingsBase
from table import *




help_text_dict = {
    'displayName': ("Name of the user suitable for display to end-users"),
    'clientSecret': ("The client secret. The client MAY omit the parameter if the client secret is an empty string"),
    'redirectUris': ("Redirection URI values used by the Client. One of these registered Redirection URI values must exactly match the redirect_uri parameter value used in each Authorization Request"),
    'responseTypes': ("A list of the OAuth 2.0 response_type values that the Client is declaring that it will restrict itself to using. If omitted, the default is that the Client will use only the code Response Type. Allowed values are code, token, id_token"),
    'applicationType': ("Kind of the application. The default, if omitted, is web. The defined values are native or web. Web Clients using the OAuth Implicit Grant Type must only register URLs using the HTTPS scheme as redirect_uris, they must not use localhost as the hostname. Native Clients must only register redirect_uris using custom URI schemes or URLs using the http scheme with localhost as the hostname"),
    'helper': ("To guide you through the fields"),

}

def accept_yes():
    get_app().exit(result=True)


def accept_no():
    get_app().exit(result=False)


def do_exit(*c):
    get_app().exit(result=False)






style = Style.from_dict(
    {
        "window.border": "#888888",
        "shadow": "bg:#222222",
        "menu-bar": "bg:#aaaaaa #888888",
        "menu-bar.selected-item": "bg:#ffffff #000000",
        "menu": "bg:#888888 #ffffff",
        "menu.border": "#aaaaaa",
        "window.border shadow": "#444444",
        "focused  button": "bg:#880000 #ffffff noinherit",
        # Styling for Dialog widgets.
        "button-bar": "bg:#4D4D4D",
        "text-area focused": "bg:#ff0000",
        "status": "reverse",

        "select-box cursor-line": "nounderline bg:ansired fg:ansiwhite",
        "select-box last-line": "underline",

    }
)

table = [
    [Label('Cliend ID',style="bg:green",), Label('Client Name',style="bg:green"), Label(
        'Grant Type',style="bg:green"), Label('Access Token',style="bg:green")],
    [Label('Cliend ID',style="bg:green",), Label('Client Name',style="bg:green"), Label(
        'Grant Type',style="bg:green"), Label('Access Token',style="bg:green")],
]


class Vertical_listbox (VSplit):
    def __init__(self, 
    children: Sequence[AnyContainer], 
    window_too_small: Optional[Container] = None,
     align: HorizontalAlign = ...,
      padding: AnyDimension = 0,
       padding_char: Optional[str] = None,
        padding_style: str = "",
         width: AnyDimension = None,
          height: AnyDimension = None,
           z_index: Optional[int] = None,
            modal: bool = False,
             key_bindings: Optional[KeyBindingsBase] = None,
              style: Union[str, Callable[[], str]] = ""
              ) -> None:
        super().__init__(children, window_too_small, align, padding, padding_char, padding_style, width, height, z_index, modal, key_bindings, style)


    def write_to_screen(
        self,
        screen: Screen,
        mouse_handlers: MouseHandlers,
        write_position: WritePosition,
        parent_style: str,
        erase_bg: bool,
        z_index: Optional[int],
    ) -> None:
        """
        Render the prompt to a `Screen` instance.

        :param screen: The :class:`~prompt_toolkit.layout.screen.Screen` class
            to which the output has to be written.
        """
        if not self.children:
            return

        children = self._all_children
        sizes = self._divide_widths(write_position.width)
        style = parent_style + " " + to_str(self.style)
        z_index = z_index if self.z_index is None else self.z_index

        # If there is not enough space.
        if sizes is None:
            self.window_too_small.write_to_screen(
                screen, mouse_handlers, write_position, style, erase_bg, z_index
            )
            return

        # Calculate heights, take the largest possible, but not larger than
        # write_position.height.
        heights = [
            child.preferred_height(width, write_position.height).preferred
            for width, child in zip(sizes, children)
        ]
        height = max(write_position.height, min(write_position.height, max(heights)))

        #
        ypos = write_position.ypos
        xpos = write_position.xpos
        
        # Draw all child panes.
        for s, c in zip(sizes, children):
            c.write_to_screen(
                screen,
                mouse_handlers,
                WritePosition(xpos, ypos, s, height),
                style,
                erase_bg,
                z_index,
            )
            xpos += s

        # Fill in the remaining space. This happens when a child control
        # refuses to take more space and we don't have any padding. Adding a
        # dummy child control for this (in `self._all_children`) is not
        # desired, because in some situations, it would take more space, even
        # when it's not required. This is required to apply the styling.
        remaining_width = write_position.xpos + write_position.width - xpos
        if remaining_width > 0:
            self._remaining_space_window.write_to_screen(
                screen,
                mouse_handlers,
                WritePosition(xpos, ypos, remaining_width, height),
                style,
                erase_bg,
                z_index,
            )




#--------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------#
class PartitionSelector:

    def __init__(self,heading,entries):
        self.heading = heading
        self.entries = entries

        self.selected_line = 1
        self.container = Window(
            content=FormattedTextControl(
                text=self._get_formatted_text,
                focusable=True,
                key_bindings=self._get_key_bindings(),
            ),
            style="class:select-box",
            height=Dimension(preferred=5, max=5),
            cursorline=True,
            right_margins=[ScrollbarMargin(display_arrows=True),],
        )

    def _get_formatted_text(self):
        result = []
        for i, entry in enumerate(self.entries):
            if i == self.selected_line:
                result.append([("[SetCursorPosition]", "")])
            result.append(entry)
            result.append("\n")

        return merge_formatted_text(result)

    def _get_key_bindings(self):
        kb = KeyBindings()

        @kb.add("up")
        def _go_up(event) -> None:
            self.selected_line = (self.selected_line - 1) % len(self.entries)

        @kb.add("down")
        def _go_up(event) -> None:
            self.selected_line = (self.selected_line + 1) % len(self.entries)

        @kb.add("enter")
        def _go_up(event) -> None:
            self.selected_line = (self.selected_line + 1) % len(self.entries)

        return kb

    def __pt_container__(self):
        return self.container
#--------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------#
class JansNavBar():
    def __init__(self, myparent, entries, select=0, bgcolor='#00ff44'):
        self.myparent = myparent
        self.navbar_entries = entries
        self.cur_navbar_selection = select
        self.bgcolor = bgcolor
        self.cur_tab = entries[self.cur_navbar_selection][0]
        self.create_window()
        self.update_status_bar()

    def create_window(self):
        self.nav_window = Window(
                            content=FormattedTextControl(
                                text=self.get_navbar_entries,
                                focusable=True,
                                key_bindings=self.get_nav_bar_key_bindings(),
                            ),
                            height=1,
                            cursorline=False,
                        )

    def get_navbar_entries(self):

        result = []
        for i, entry in enumerate(self.navbar_entries):
            if i == self.cur_navbar_selection:
                result.append(HTML('<style fg="ansired" bg="{}">{}</style>'.format(self.bgcolor, entry[1])))
            else:
                result.append(HTML('<b>{}</b>'.format(entry[1])))
            result.append("   ")

        
        return merge_formatted_text(result)


    def update_status_bar(self):
        self.cur_tab = self.navbar_entries[self.cur_navbar_selection][0]
        self.myparent.update_status_bar("Container for " + self.navbar_entries[self.cur_navbar_selection][1])


    def get_nav_bar_key_bindings(self):
        kb = KeyBindings()

        @kb.add("left")
        def _go_up(event) -> None:
            self.cur_navbar_selection = (self.cur_navbar_selection - 1) % len(self.navbar_entries)
            self.update_status_bar()

        @kb.add("right")
        def _go_up(event) -> None:
            self.cur_navbar_selection = (self.cur_navbar_selection + 1) % len(self.navbar_entries)
            self.update_status_bar()

        return kb
#--------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------#

class JansCliApp(Application):

    def __init__(self):
        self.set_keybindings()
        self.containers = {}


        self.yes_button = Button(text="Yes", handler=accept_yes)
        self.no_button = Button(text="No", handler=accept_no)
        self.status_bar = TextArea(style="class:status", height=1, focusable=False)

        self.prapare_containers()

        self.nav_bar = JansNavBar(
                    self,
                    entries=[('oauth', 'Auth Server'), ('fido', 'FDIO'), ('scim', 'SCIM'), ('config_api', 'Config-API'), ('client_api', 'Client-API'), ('scripts', 'Scripts')],
                    select=0
                    )

        self.center_frame = Frame(
                                body = DynamicContainer(self.my_container), 
                                height=D())

        

        self.root_layout = HSplit(
                    [
                        Frame(self.nav_bar.nav_window),
                        self.center_frame,
                        self.status_bar
                    ],
                )

        super(JansCliApp, self).__init__(
                layout=Layout(self.root_layout),
                key_bindings=self.bindings, 
                style=style, 
                full_screen=True
            )


    def focus_next(self, ev):
        focus_next(ev)
        self.update_status_bar()

    def focus_previous(self, ev):
        focus_previous(ev)
        self.update_status_bar()

    def set_keybindings(self):
        # Global key bindings.
        self.bindings = KeyBindings()
        self.bindings.add("tab")(self.focus_next)
        self.bindings.add("s-tab")(self.focus_previous)
        self.bindings.add("c-c")(do_exit)




    def prapare_containers(self):

        self.nav_bar_oauth = JansNavBar(
                    self,
                    entries=[('oaut:clients', 'Clients'), ('oaut:scopes', 'Scopes'), ('oaut:keys', 'Keys'), ('oaut:defaults', 'Defaults'), ('oaut:properties', 'Properties'), ('oaut:logging', 'Logging')],
                    select=0,
                    bgcolor='#66d9ef'
                    )

        self.containers['oauth'] = HSplit([
                    Box(self.nav_bar_oauth.nav_window, style='fg:#f92672 bg:#4D4D4D', height=1),
                    self.getTitledText("Display Name:", name='displayName'),
                    self.getTitledText("Client Secret:", name='clientSecret'),
                    self.getTitledText("Redirect Uris:", name='redirectUris', height=3),
                    self.getTitledCheckBox("Response Types:", name='responseTypes', values=['code', 'token', 'id_token']),
                    self.getTitledRadioButton("Application Type:", name='applicationType', values=['web', 'native']),
                    HSplit([Box(body=VSplit([self.yes_button, self.no_button], align="CENTER", padding=3), style="class:button-bar", height=1)],
                        height=D(),
                        align = VerticalAlign.BOTTOM,
                        )
                    ],
                )

        self.containers['fido'] = Vertical_listbox([
            # HSplit([Label(text='Client ID',width=15),]),
            # Window(width=1, char="|"),
            # HSplit([Label(text='Client Name',width=15),]),
            # Window(width=1, char="|"),
            # HSplit([Label(text='Grant Types',width=15),]),
            # Window(width=1, char="|"),

                    # PartitionSelector(heading = ['Cliend ID', 'Client Name','Grant Type' , 'Access Token']
                    #     ,entries=[
                    #     HTML("<bold>Cliend ID</bold>        <bold>Client Name</bold>         <bold>Grant Type</bold>         <bold>Access Token</bold>"),
                    #     ]
                    # )  


                   Table(
                        table=table,
                        column_width=D.exact(15),
                        borders=ThickBorder),
            

            
                        # Window(width=6, char=" "),
            
     
                ],
            )    


        self.containers['NA'] = HSplit([Label(text="Not imlemented yet"), Button(text="MyButton")], width=D())


    def my_container(self):

        cur_tab = self.nav_bar.cur_tab

        self.center_frame.title = self.nav_bar.navbar_entries[self.nav_bar.cur_navbar_selection][1]

        if cur_tab in self.containers:
            return self.containers[cur_tab]

        return self.containers['NA']


    def getTitledText(self, title, name, height=1):
        multiline = height > 1
        ta = TextArea(multiline=multiline)
        ta.window.jans_name = name
        return VSplit([Label(text=title, width=len(title)+1), ta], height=height)

    def getTitledCheckBox(self, title, name, values):
        cb = CheckboxList(values=[(o,o) for o in values])
        cb.window.jans_name = name
        return VSplit([Label(text=title, width=len(title)+1), cb])


    def getTitledRadioButton(self, title, name, values):
        rl = RadioList(values=[(option, option) for option in values])
        rl.window.jans_name = name
        return VSplit([Label(text=title, width=len(title)+1), rl],
                height=len(values)
            )

    def get_statusbar_text(self):
        wname = getattr(self.layout.current_window, 'jans_name', 'NA')
        return help_text_dict.get(wname, '')

    def update_status_bar(self, text=None):
        if text:
            self.status_bar.text
        else:
            wname = getattr(self.layout.current_window, 'jans_name', 'NA')
            text = help_text_dict.get(wname, '')

        open("tmp/h.txt", "a").write(text+'\n')
        self.status_bar.text = text


application = JansCliApp()

def run():
    result = application.run()
    print("You said: %r" % result)


if __name__ == "__main__":
    run()
