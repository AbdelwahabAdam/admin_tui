
#!/usr/bin/env python3
import curses
from time import time
import npyscreen
import weakref


######################### Classes to inherit from ########################

class InputWidget(npyscreen.TitleText):
    def __init__(self, *args, **keywords):
        super(InputWidget, self).__init__(*args, **keywords)
        self.name = 'test'
##########################################################################
class InputBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.TitleText
    _contained_widget_height = 2
##########################################################################
class multiContainedBox(npyscreen.BoxTitle):
    _contained_widget = [InputWidget, InputWidget,InputWidget]

    def make_contained_widget(self, contained_widget_arguments=None):
        self._my_widgets = []
        _rely = self.rely+1
        _relx = self.relx+2
        for widget in self._contained_widget :
            self._my_widgets.append(widget(self.parent,
                                    rely=_rely, relx = _relx,
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
class MyGrid_H(npyscreen.GridColTitles):       
    def custom_print_cell(self, actual_cell, cell_display_value):
        
        if cell_display_value in ["Auth Server", "FIDO","SCIM",
                     "Config-API","Client-API", "Scripts"]:
           actual_cell.color = 'FORMDEFAULT'
##########################################################################
class InputBox_H(npyscreen.BoxTitle):
    _contained_widget = MyGrid_H
##########################################################################
class MainForm(npyscreen.FormBaseNew):
    def create(self):
        self.add_handlers({"^T": self.change_forms})
        y, x = self.useable_space()
        ####################   Title of the screen      
        self.Title = self.add(npyscreen.TitleText, name="Jassan admin", value=None, editable = None)
        ####################   The  Main Navigation     
        self.gd = self.add(InputBox_H, name="",max_height=5,max_width=110,relx=1, rely=3)
        self.gd.values = []
        self.gd.values.append(["Auth Server", "FIDO","SCIM","Config-API","Client-API", "Scripts"])   
        # self.InputBox = self.add(multiContainedBox, name="Header",max_height=5,max_width=110,relx=1, rely=3,value='hopa')
        
        #####################    The Side Navigation      
        self.list = self.add(npyscreen.BoxTitle, name="",
                    custom_highlighting=True, values=["Basic", "Token","Logout","Timeout","URIs", "Encription","Client Properties", "Client Scripts","Save"],
                     value=[],max_height=20,max_width=24, relx=1, rely=8)

        # self.InputBox2 = self.add(multiContainedBox, name="Side", max_height=20, max_width=24, relx=1, rely=8,value='asdf')
        
        ####################     The Main Content      
        self.InputBox3 = self.add(multiContainedBox, name="Content", max_height=20, max_width=86, relx=25, rely=8,value="main content",color='FORMDEFAULT')
       
        ####################      END            
    def on_ok(self):
        # Exit the application if the OK button is pressed.
        self.parentApp.switchForm(None)

    def change_forms(self, *args, **keywords):
        if self.name == "Navigate 1":
            change_to = "SECOND"
        elif self.name == "Navigate 2":
            change_to = "THIRD"
        else:
            change_to = "MAIN"

        self.parentApp.change_form(change_to)
### y = 30
### x = 119




############################### Start poing  ####################################
class MainAllForms(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN",       MainForm, name="Navigate 1", color="DANGER",)
        self.addForm("SECOND",     MainForm, name="Navigate 2", color="GOODHL",  )
        self.addForm("THIRD", MainForm, name="Navigate 3", color="CAUTION",)
        
    def onCleanExit(self):
        npyscreen.notify_wait("Goodbye!")
    
    def change_form(self, name):
        self.switchForm(name)     
        self.resetHistory()



MyApp = MainAllForms()
MyApp.run()