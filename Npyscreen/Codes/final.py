#!/usr/bin/env python3
import curses
import npyscreen

######################### Classes to inherit from ########################



class InputBox(npyscreen.TitleText):
    _contained_widget = npyscreen.TitleText
    _contained_widget_height = 2
    def __init__(self, *args, **keywords):
        super(InputBox, self).__init__(*args, **keywords)
        self.name = 'test'
##########################################################################


class multiContainedBox(npyscreen.BoxTitle):
    _contained_widget = [InputBox, InputBox, InputBox]

    def make_contained_widget(self, contained_widget_arguments=None):
        self._my_widgets = []
        _rely = self.rely+1
        _relx = self.relx+2
        for widget in self._contained_widget:
            self._my_widgets.append(widget(self.parent,
                                    rely=_rely, relx=_relx,
                                    max_width=self.width, max_height=10,
                                           ))
        self.entry_widget = self._my_widgets[1]

    def update(self, clear=True):
        if self.hidden and clear:
            self.clear()
            return False
        elif self.hidden:
            return False
        super(multiContainedBox, self).update(clear=clear)
        for w in self._my_widgets:
            w.update(clear=clear)
##########################################################################

##########################################################################


class MainForm(npyscreen.FormBaseNew):
    def create(self):
        self.add_handlers({'^T': self.fun})
        y, x = self.useable_space()
        # Title of the screen
        self.Title = self.add(npyscreen.TitleText,
                              name="Title1", value=None, editable=None)
        # The Side Navigation
        # self.list = self.add(npyscreen.BoxTitle, name="",
        #                      custom_highlighting=True, values=["Selection1", "Selection2", "Selection3", "Selection4",],
        #                      value="Basic", max_height=20, max_width=24, relx=1, rely=8)

        # # The Main Content
        # self.InputBox3 = self.add(multiContainedBox, name="Content", max_height=20,
        #                           max_width=86, relx=25, rely=8, value="main content", color='FORMDEFAULT')

    def create_widgets_from_list(self, widget_list):
            # This code is currently experimental, and the API may change in future releases
            (npyscreen.TextBox, {'rely': 2, 'relx': 7, 'editable': False})
            for line in widget_list:
                w_type   = line[0]
                keywords = line[1]
                self.add_widget(w_type, **keywords) 


        # END
    def on_ok(self):
        # Exit the application if the OK button is pressed.
        self.list.value = "Not Changed"


    def fun(self, *args, **keywords):
        if self.list.value == "Logout" :
            self.list.value = "changed"
        else :
            self.list.value = "Not Changed"

    ### y = 30
    ### x = 119


class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="")


MyApp = App()
MyApp.run()