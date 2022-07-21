#!/usr/bin/env python3

import sys
from asciimatics.widgets import Frame, ListBox, Layout, Label, Divider, Text, \
    Button, TextBox, Widget, CheckBox, DropdownList, ListBox, RadioButtons
from asciimatics.widgets.popupdialog import PopUpDialog

from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
# from my_checkbox import checkBoxButtons

help_text_dict = {
    'displayName': "Name of the user suitable for display to end-users",
    'clientSecret': "The client secret. The client MAY omit the parameter if the client secret is an empty string",
    'redirectUris': "Redirection URI values used by the Client. One of these registered Redirection URI values must exactly match the redirect_uri parameter value used in each Authorization Request",
    "responseTypes": "A list of the OAuth 2.0 response_type values that the Client is declaring that it will restrict itself to using. If omitted, the default is that the Client will use only the code Response Type. Allowed values are code, token, id_token",
    }

class CLIFrame(Frame):

    def __init__(self, screen, title='CLI Frame'):
        super().__init__(screen,
                                   screen.height,
                                   screen.width,
                                   has_border=True,
                                   can_scroll=True,
                                   )

        
        self.title = title
        self.layout = Layout([100], fill_frame=True)
        self.add_layout(self.layout)

        self.button_layout = Layout([1, 1, 1, 1])
        self.add_layout(self.button_layout)

        self.status = Layout([1])
        self.add_layout(self.status)
        self.status.add_widget(Divider())
        self.help_text = Label('Help')
        self.status.add_widget(self.help_text)

    # def checkBoxButtons(self,name='',items=()):
    #     for i, o in enumerate(items):
    #         label = "{}:".fornat(name) if i==0 else None
    #         self.layout.add_widget(CheckBox(label=label, text=o,  name="responseTypes:{}".format(o), on_focus=self.update_help))



    def update_help(self):
        cur_widget = self.layout.get_current_widget()
        help_key = cur_widget.name.split(':')[0]
        self.help_text.text = help_text_dict.get(help_key, help_key)
        self.help_text.update(None)

    def reset(self):
        super(CLIFrame, self).reset()

class OpenIDClientForm(CLIFrame):
    def __init__(self, screen):
        CLIFrame.__init__(self, screen, "OpenID Client")

        self.layout.add_widget(Text("Display Name:", "displayName", on_focus=self.update_help))
        self.layout.add_widget(Text("Client Secret:", "clientSecret", on_focus=self.update_help))
        self.layout.add_widget(TextBox(label="Redirect Uris:", name="redirectUris", height=3, on_focus=self.update_help, as_string=True))

        # self.checkBoxButtons(name='responseTypes', items = ('code', 'token', 'id_token') )

        
        # for i, o in enumerate(('code', 'token', 'id_token')):
        #     label = "Response Types:" if i==0 else None
        #     self.layout.add_widget(CheckBox(label=label, text=o,  name="responseTypes:{}".format(o), on_focus=self.update_help))


        self.button_layout.add_widget(Button("OK", self._ok), 0)
        self.button_layout.add_widget(Button("Next", self._next), 3)

        self.fix()


    def _ok(self):
        self.save()
        #self._model.update_current_contact(self.data)
        raise NextScene("Main")

    def _next(self):
        raise NextScene("Test")


class TestForm(CLIFrame):
    def __init__(self, screen):
        CLIFrame.__init__(self, screen, "Test Form")
        self.layout.add_widget(Text("Test Name :", "testName", on_focus=self.update_help))
        self.fix()

def jans_cli_app(screen, scene):
    scenes = [
        Scene([OpenIDClientForm(screen)], -1, name="OpenIDClientForm"),
        Scene([TestForm(screen)], -1, name="Test"),
    ]

    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)

last_scene = None

while True:
    try:
        Screen.wrapper(jans_cli_app, catch_interrupt=True, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene
