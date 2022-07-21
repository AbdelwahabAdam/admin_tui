
#!/usr/bin/env python3
import npyscreen

######################### Classes to inherit from ########################
class InputWidget(npyscreen.TitleText):
    def __init__(self, screen,na=None, begin_entry_at=16, field_width=None, value=None, use_two_lines=None, hidden=False, labelColor='LABEL', allow_override_begin_entry_at=True, **keywords):
        super().__init__(screen, begin_entry_at, field_width, value, use_two_lines, hidden, labelColor, allow_override_begin_entry_at, **keywords)


##########################################################################
class multiContainedBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.TitleText



    def __init__(self, screen, contained_widget_arguments=None,typeof = None,form_asW=None,passed_widget=None, *args, **keywords):
        super().__init__(screen, contained_widget_arguments, *args, **keywords)
        self._my_widgets = []
        self.passed_widget = passed_widget
        self.typeof = typeof
        self.form = form_asW


        if  self.typeof == 'user':
             self.passed_widget.name = "Heading"
             self.passed_widget.values =self.form.add(npyscreen.TitleSelectOne, name="hopa",
                values = ["op1","op3","op2"], scroll_exit=True)

        self.form.name = "content 3"


    def make_contained_widget(self,form_asW=None, contained_widget_arguments=None):
        self.form = form_asW
        self._my_widgets = []
        _rely = self.rely+1
        _relx = self.relx+2
        self._my_widgets.append(self._contained_widget(self.parent,rely=_rely, relx = _relx,max_width=self.width, max_height=10,))

        
        self.entry_widget = self._my_widgets[0]


##########################################################################

class MainForm(npyscreen.FormBaseNew):

    
    def create(self):
        y, x = self.useable_space()
        ####################   Title of the screen      
        Title = self.add(npyscreen.TitleText, name="Jassan admin", value="title text value", editable = None)
        ####################   The  Main Navigation     

        header = self.add(multiContainedBox, name="Header",max_height=15,max_width=110,relx=1,
          rely=3,value='hopa',typeof='admin',passed_widget = Title,form_asW = self,values = [])


        ####################     The Main Content      
        self.cont =  self.add(multiContainedBox, name="Content", max_height=20, max_width=86, relx=25, 
        rely=8,value="main content",color='FORMDEFAULT',passed_widget = header,typeof='user',form_asW = self)
       
        ####################      END            
    def on_ok(self):
        # Exit the application if the OK button is pressed.
        self.parentApp.switchForm("SECOND")


### y = 30
### x = 119




############################### Start poing  ####################################
class MainAllForms(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN",       MainForm, name="", color="GOODHL",)
        
    def onCleanExit(self):
        npyscreen.notify_wait("Goodbye!")
    




MyApp = MainAllForms()
MyApp.run()


