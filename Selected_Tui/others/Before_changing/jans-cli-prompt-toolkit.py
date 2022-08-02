#!/usr/bin/env python3
"""
"""

#   0a87ab07-5d9e-41dd-a3cb-9fd8d59fc3c3
#   Partner Portal  
#   password
#   JWT

from unicodedata import name
from prompt_toolkit.formatted_text import HTML, merge_formatted_text
from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.layout.containers import Float, HSplit, VSplit, Window
from prompt_toolkit.layout.containers import (
    Dimension,
    Float,
    HSplit,
    VSplit,
    Window,
    DynamicContainer,
    ConditionalContainer,
    FloatContainer,
)
from prompt_toolkit.layout.margins import ScrollbarMargin
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.containers import VerticalAlign
from prompt_toolkit.layout.dimension import D
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import (
    Box,
    Button,
    Dialog,
    Frame,
    Label,
    RadioList,
    TextArea,
    CheckboxList,
    Shadow,
)
from prompt_toolkit.filters import Condition
from functools import partial
from Custom_Dialog import Custom_Dialog

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


#--------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------#


class Custom_PartitionSelector:

    def __init__(self, headers, data=None):

        self.headers = headers  # '     '.join(headers)
        self.dialog_visible = False
        self.selected_line = 1
        self.data = data
        self.spaces = []
        self.handel_spaces()
        
        self.ClientID = TextArea(height=1,multiline=False)
        self.ClientName = TextArea(height=1,multiline=False)
        self.GrantType = TextArea(height=1,multiline=False)
        self.AccessToken = TextArea(height=1,multiline=False)
        self.Helper = TextArea(height=1,multiline=False,focusable=False)

        if self.data == None:
            self.data = [['No Cliend ID', 'No Client Name',
                          'No Grant Type', 'No Access Token']]

        self.dialog = Dialog(
            title="Add New user",
            body=HSplit(
                [
                    VSplit([Label(text="Please type Client ID:", dont_extend_height=True),
                            self.ClientID, ]),
                    Window(height=1, char="."),
                    VSplit([Label(text="Please type Client Name:", dont_extend_height=True),
                            self.ClientName, ]),
                    Window(height=1, char="."),
                     VSplit([Label(text="Please type Grant Type:", dont_extend_height=True),
                            self.GrantType, ]),
                     Window(height=1, char="."),
                     VSplit([Label(text="Please type Access Token:", dont_extend_height=True),
                            self.AccessToken, ]),  
                     Window(height=1, char="."),
                     self.Helper,

                ],
                padding=Dimension(preferred=1, max=1),
            ),
            buttons=[
                Button(
                    text="OK",
                    handler=self.save_dialog,
                ),
                Button(
                    text="Cancel",
                    handler=self.hide_dialog,
                ),
            ],
            with_background=True,
            width=100,
        )
        
        self.container = FloatContainer(
            content=HSplit([
                VSplit([
                    self.getTitledText("Search:", name='displayName'),
                    Button(text='Add Client', left_symbol='',
                           right_symbol='', handler=partial(self.add_client))
                ]),
                Window(height=1),
                Window(height=1, char="."),
                Window(height=1),
                Window(
                    content=FormattedTextControl(
                        text=self._get_head_text,
                        focusable=False,
                        style='green',
                    ),
                    style="class:select-box",
                    height=Dimension(preferred=1, max=1),
                    cursorline=False,
                ),
                 Window(height=1),
                Window(
                    content=FormattedTextControl(
                        text=self._get_formatted_text,
                        focusable=True,
                        key_bindings=self._get_key_bindings(),
                        style='white',
                    ),
                    style="class:select-box",
                    height=Dimension(preferred=5, max=5),
                    cursorline=True,
                    right_margins=[ScrollbarMargin(display_arrows=True), ],
                ),
                 Window(height=10),
                                 
     
            
            ]
            ),
            floats=[
                Float(
                    ConditionalContainer(
                        Shadow(self.dialog),
                        filter=Condition(lambda: self.dialog_visible),

                    )
                )
            ],


        )
#--------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------#
    def handel_spaces(self):
        datalen = []
        for dataline in range(len(self.data)) :
            line = []
            for i in  self.data[dataline]:
                line.append(len(i))
            datalen.append(line)
        dict = {}
        for num in range(len(datalen[0])) :
            dict[num] = []

        for k in range(len(datalen)) :
            for i in range(len(datalen[k])):
                dict[i].append(datalen[k][i])

        for i in dict :
            self.spaces.append(max(dict[i]))

   
   
   
    def hide_dialog(self):
        self.dialog_visible = False
        get_app().layout.focus(self.container)
    
    def save_dialog(self):
        
        if self.ClientID.text and self.ClientName.text and self.GrantType.text and self.AccessToken.text :
            if len (self.ClientID.text) == 36 :
                x =[]
                x.append(self.ClientID.text)
                x.append(self.ClientName.text)
                x.append(self.GrantType.text)
                x.append(self.AccessToken.text)

                self.data.append(x)
                self.dialog_visible = False
                get_app().layout.focus(self.container)
            else :
                self.Helper.text = 'Please Insert valid Clined ID'
        else :
            self.Helper.text = 'Please Fill All fields'

#--------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------#
    def getTitledText(self, title, name, height=1):
        multiline = height > 1
        ta = TextArea(multiline=multiline)
        ta.window.jans_name = name
        return VSplit([Label(text=title, width=len(title)+1), ta], height=height)

    def _get_head_text(self):
        result = []
        # result.append(self.heading)
        # result.append("\n")
        y = ''
        for k in range(len(self.headers)):
            y += self.headers[k] + ' ' * \
                (len(self.data[0][k]) - len(self.headers[k]) + 5)
        result.append(y)
        result.append("\n")

        return merge_formatted_text(result)

#--------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------#
    def add_client(self):
        self.dialog_visible = True
        # event.app.layout.focus(self.dialog)
#--------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------#
    def _get_formatted_text(self):
        result = []
        for i, entry in enumerate(self.data):
            if i == self.selected_line:
                result.append([("[SetCursorPosition]", "")])
            result.append('     '.join(entry))
            result.append("\n")

        return merge_formatted_text(result)
#--------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------#

    def _get_key_bindings(self):
        kb = KeyBindings()

        @kb.add("up")
        def _go_up(event) -> None:
            self.selected_line = (self.selected_line - 1) % len(self.data)

        @kb.add("down")
        def _go_up(event) -> None:
            self.selected_line = (self.selected_line + 1) % len(self.data)

        @kb.add("enter")
        def _(event):

            self.dialog_visible = True
            event.app.layout.focus(self.dialog)

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
                result.append(
                    HTML('<style fg="ansired" bg="{}">{}</style>'.format(self.bgcolor, entry[1])))
            else:
                result.append(HTML('<b>{}</b>'.format(entry[1])))
            result.append("   ")

        return merge_formatted_text(result)

    def update_status_bar(self):
        self.cur_tab = self.navbar_entries[self.cur_navbar_selection][0]
        self.myparent.update_status_bar(
            "Container for " + self.navbar_entries[self.cur_navbar_selection][1])

    def get_nav_bar_key_bindings(self):
        kb = KeyBindings()

        @kb.add("left")
        def _go_up(event) -> None:
            self.cur_navbar_selection = (
                self.cur_navbar_selection - 1) % len(self.navbar_entries)
            self.update_status_bar()

        @kb.add("right")
        def _go_up(event) -> None:
            self.cur_navbar_selection = (
                self.cur_navbar_selection + 1) % len(self.navbar_entries)
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
        self.status_bar = TextArea(
            style="class:status", height=1, focusable=False)

        self.prapare_containers()

        self.nav_bar = JansNavBar(
            self,
            entries=[('oauth', 'Auth Server'), ('fido', 'FDIO'), ('scim', 'SCIM'), (
                'config_api', 'Config-API'), ('client_api', 'Client-API'), ('scripts', 'Scripts')],
            select=0
        )

        self.center_frame = Frame(
            body=DynamicContainer(self.my_container),
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
            entries=[('oaut:clients', 'Clients'), ('oaut:scopes', 'Scopes'), ('oaut:keys', 'Keys'), (
                'oaut:defaults', 'Defaults'), ('oaut:properties', 'Properties'), ('oaut:logging', 'Logging')],
            select=0,
            bgcolor='#66d9ef'
        )

        self.containers['oauth'] = HSplit([
            Box(self.nav_bar_oauth.nav_window,
                style='fg:#f92672 bg:#4D4D4D', height=1),
            self.getTitledText("Display Name:", name='displayName'),
            self.getTitledText("Client Secret:", name='clientSecret'),
            self.getTitledText(
                "Redirect Uris:", name='redirectUris', height=3),
            self.getTitledCheckBox("Response Types:", name='responseTypes', values=[
                                   'code', 'token', 'id_token']),
            self.getTitledRadioButton(
                "Application Type:", name='applicationType', values=['web', 'native']),
            HSplit([Box(body=VSplit([self.yes_button, self.no_button], align="CENTER", padding=3), style="class:button-bar", height=1)],
                   height=D(),
                   align=VerticalAlign.BOTTOM,
                   )
        ],
        )

        self.containers['fido'] = HSplit([

            # VSplit([
            #     self.getTitledText("Search:", name='displayName'),
            #     Button(text='Add Client', left_symbol='', right_symbol='',handler=partial(add_client))
            # ]),


            Custom_PartitionSelector(
                headers=['Cliend ID', 'Client Name',
                         'Grant Type', 'Access Token'],
                data=[
                    ['69574504-28f0-4e96-a0ec-fffdd0f26ea0', 'Support portal',
                     'authorization_code', 'JWT'],
                    ['c64bc7a2-ff35-4166-8174-9436f74d4c38', 'Ecommerce Site',
                     'authorization_code', 'Reference'],
                ],
            ),


        ],
        )

        self.containers['NA'] = HSplit(
            [Label(text="Not imlemented yet"), Button(text="MyButton")], width=D())

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
        cb = CheckboxList(values=[(o, o) for o in values])
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
