from asciimatics.widgets import Frame, ListBox, Layout, Label, Divider, Text, \
    Button, TextBox, Widget, CheckBox, DropdownList, ListBox, RadioButtons

class checkBoxButtons(Widget):

    def __init__(self, items,name, tab_stop=True, disabled=False, on_focus=None, on_blur=None):
        super().__init__(name,items, tab_stop, disabled, on_focus, on_blur)

        # for i, o in enumerate(items):
        #     label = "{}:".fornat(name) if i==0 else None
        #     self.layout.add_widget(CheckBox(label=label, text=o,  name="responseTypes:{}".format(o), on_focus=self.update_help))

