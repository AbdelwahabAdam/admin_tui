#!/usr/bin/env python3

from asciimatics.widgets import Frame, ListBox, Layout, Label, Divider, Text, \
    Button, TextBox, Widget, CheckBox, DropdownList, ListBox, RadioButtons
from asciimatics.widgets.popupdialog import PopUpDialog

from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
from sqlalchemy import column

help_text_dict = {
    'displayName': "Name of the user suitable for display to end-users",
    'clientSecret': "The client secret. The client MAY omit the parameter if the client secret is an empty string",
    'redirectUris': "Redirection URI values used by the Client. One of these registered Redirection URI values must exactly match the redirect_uri parameter value used in each Authorization Request"
    "description:" "A list of the OAuth 2.0 response_type values that the Client is declaring that it will restrict itself to using. If omitted, the default is that the Client will use only the code Response Type. Allowed values are code, token, id_token",
    }


class Custom_checkbox (CheckBox):

    def update(self, frame_no):
        self._draw_label()

        # Render this checkbox.
        check_char = u"✓"
        (colour, attr, bg) = self._pick_colours("control", self._has_focus)
        self._frame.canvas.print_at(
            "[{}] ".format(check_char if self._value else " "),
            self._x + self._offset,
            self._y,
            colour, attr, bg)
        (colour, attr, bg) = self._pick_colours("field", self._has_focus)
        self._frame.canvas.print_at(
            self._text,
            self._x + self._offset + 4,
            self._y,
            colour, attr, bg)

class OpenIDClientForm(Frame):
    def __init__(self, screen):
        super(OpenIDClientForm, self).__init__(screen,
                                       screen.height,
                                       screen.width,
                                       has_border=True,
                                       can_scroll=True,
                                       title="Open ID Client")

        self.layout = Layout([100], fill_frame=False)
        self.add_layout(self.layout)
        self.layout.add_widget(Text("displayName:", "displayName", on_focus=self.update_help))
        self.layout.add_widget(Text("clientSecret:", "clientSecret", on_focus=self.update_help))
        self.layout.add_widget(TextBox(label="redirectUris:", name="redirectUris", height=3, on_focus=self.update_help, as_string=True))
        self.layout.add_widget(Divider())

        cb_layout = Layout(columns=[2,2,2,5,], fill_frame=True)
        self.add_layout(cb_layout)
        cb_layout.add_widget(Label('responseTypes')) 
        for i, o in enumerate(('code', 'token', 'id_token')):
            cb_layout.add_widget(Custom_checkbox(text=o,), i+1)
        

        # cb_layout2 = Layout(columns=[1,1,1,1,], fill_frame=False)
        # self.add_layout(cb_layout2)
        # cb_layout2.add_widget(Label('responseTypes')) 
        # for i, o in enumerate(('code', 'token', 'id_token')):
        #     cb_layout2.add_widget(Label("Name:",align='^'),i+1)


        # cb_layout3 = Layout(columns=[1,1,1,1,], fill_frame=True)
        # self.add_layout(cb_layout3)
        # cb_layout3.add_widget(Label('responseTypes')) 
        # for i, o in enumerate(('code', 'token', 'id_token')):
        #     cb_layout3.add_widget(Label("Name:",align='>'),i+1)


        

        layout2 = Layout([1, 1, 1, 1],)
        self.add_layout(layout2)
        layout2.add_widget(Button("OK", self._ok), 0)
        layout2.add_widget(Button("Cancel", self._cancel), 3)
        
        self.layout3 = Layout([1])
        self.add_layout(self.layout3)
        self.layout3.add_widget(Divider())
        self.help_text = Label('Help')
        self.layout3.add_widget(self.help_text)
        self.fix()

    def reset(self):
        super(OpenIDClientForm, self).reset()

    def _ok(self):
        self.save()
        #self._model.update_current_contact(self.data)
        raise NextScene("Main")

    @staticmethod
    def _cancel():
        raise NextScene("Main")


    def update_help(self):
        cur_widget = self.layout.get_current_widget()
        self.help_text.text = help_text_dict.get(cur_widget.name, '')
        self.help_text.update(None)


def jans_cli_app(screen, scene):
    scenes = [
        Scene([OpenIDClientForm(screen)], -1, name="OpenIDClientForm"),
    ]

    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)

last_scene = None

while True:
    try:
        Screen.wrapper(jans_cli_app, catch_interrupt=True, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene
