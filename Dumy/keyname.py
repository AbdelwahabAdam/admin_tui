# #! /usr/bin/env python3
# # coding:utf8

# import npyscreen

# # content
# headers = ["column 1", "column 2", "column 3", "column 4"]
# entries = [["a1", "a2", "a3", "a4"],
#            ["b1", "b2", "b3", "b4"],
#            ["c1", "c2", "c3", "c4"],
#            ["d1", "d2", "d3", "d4"],
#            ["e1", "e2", "e3", "e4"]]

# # returns a string in which the segments are padded with spaces.
# def format_entry(entry):
#     return "{:10} | {:10} | {:10} | {:10}".format(entry[0], entry[1] , entry[2], entry[3])

# class SecondForm(npyscreen.Form):
#     def on_ok(self):
#         self.parentApp.switchFormPrevious()
#         # add the widgets of the second form
#     def create(self):
#         self.col1 = self.add(npyscreen.TitleText, name="column 1:")
#         self.col2 = self.add(npyscreen.TitleText, name="column 2:")
#         self.col3 = self.add(npyscreen.TitleText, name="column 3:")
#         self.col4 = self.add(npyscreen.TitleText, name="column 4:")

#     def afterEditing(self):
#         self.parentApp.setNextForm("MAIN")

# class MainForm(npyscreen.Form):
#     def on_ok(self):
#         self.parentApp.switchForm(None)

#     def changeToSecondForm(self):
#         self.parentApp.change_form("SECOND")

#     # add the widgets of the main form
#     def create(self):
#         self.add(npyscreen.FixedText, value=format_entry(headers), editable=False, name="header")

#         for i, entry in enumerate(entries):
#             self.add(npyscreen.ButtonPress, when_pressed_function=self.changeToSecondForm, name=format_entry(entry))


# class TestTUI(npyscreen.NPSAppManaged):
#     def onStart(self):
#         self.addForm("MAIN", MainForm)
#         self.addForm("SECOND", SecondForm, name="Edit row")

#     def onCleanExit(self):
#         npyscreen.notify_wait("Goodbye!")

#     def change_form(self, name):
#         self.switchForm(name)


# if __name__ == "__main__":
#     tui = TestTUI()
#     tui.run()


# !/usr/bin/env python
### encoding: utf-8
#!/usr/bin/env python
import npyscreen, curses

class MyTestApp(npyscreen.NPSAppManaged):
    def onStart(self):
        # When Application starts, set up the Forms that will be used.
        # These two forms are persistent between each edit.
        self.addForm("MAIN",       MainForm, name="Screen 1", color="IMPORTANT",)
        self.addForm("SECOND",     MainForm, name="Screen 2", color="WARNING",  )
        # This one will be re-created each time it is edited.
        self.addFormClass("THIRD", MainForm, name="Screen 3", color="CRITICAL",)
        
    def onCleanExit(self):
        npyscreen.notify_wait("Goodbye!")
    
    def change_form(self, name):
        # Switch forms.  NB. Do *not* call the .edit() method directly (which 
        # would lead to a memory leak and ultimately a recursion error).
        # Instead, use the method .switchForm to change forms.
        self.switchForm(name)
        
        # By default the application keeps track of every form visited.
        # There's no harm in this, but we don't need it so:        
        self.resetHistory()
    
class MainForm(npyscreen.ActionForm):
    def create(self):
        self.add(npyscreen.TitleText, name = "Text:", value= "Press ^T to change screens" )
        
        self.add_handlers({"^T": self.change_forms})

    def on_ok(self):
        # Exit the application if the OK button is pressed.
        self.parentApp.switchForm(None)

    def change_forms(self, *args, **keywords):
        if self.name == "Screen 1":
            change_to = "SECOND"
        elif self.name == "Screen 2":
            change_to = "THIRD"
        else:
            change_to = "MAIN"

        # Tell the MyTestApp object to change forms.
        self.parentApp.change_form(change_to)
    
    


def main():
    TA = MyTestApp()
    TA.run()


if __name__ == '__main__':
    main()