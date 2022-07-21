#!/usr/bin/env python3

import npyscreen
import curses
import curses.ascii

class App (npyscreen.StandardApp):
  def onStart (self):
    self.addForm ("MAIN", MainForm, name = "My Form")

class MainForm (npyscreen.ActionForm):
  # Constructor
  def create (self):
    # Add the TitleText widget to the form
    self.w_some_name = self.add (npyscreen.TitleText, name = "Some Name", value = "Joe Blogs")
    self.w_some_name_info = self.add(npyscreen.FixedText, value = "Time")
    self.w_next_control = self.add (npyscreen.TitleText, name = "Next Control", value = "Can't advance to me :-(")

    # Actually want an event only when the text in the control "some_name" changes.  But I don't think such a
    # "text has been changed, about to move to the next control" event exists in npyscreen ?
    # The closest I can do is find any way that the control can be moved away from (TAB, New Line etc) - and
    # trap the event that way
    self.w_some_name.add_handlers({curses.ascii.NL: self.some_name_changed,
        curses.ascii.CR: self.some_name_changed,
        curses.ascii.TAB: self.some_name_changed,
        curses.KEY_DOWN: self.some_name_changed,
        curses.KEY_UP: self.some_name_changed})

  def some_name_changed(self, input):
    # Do something dynamically based on the text in some_name.  For proof of concept, write out the length of the string
    self.w_some_name_info.value = "The length of the above string in the above control is %d" % len(self.w_some_name.value)
    self.w_some_name_info.display()
    # Have successfully managed to dynamically update a control (w_some_name_info) based on w_some_name changing
    # But the problem now is that I'm stuck on w_some_name, and there doesn't seem to be a way to progmatically advance
    # to the next control in the form

  def on_cancel (self):
    self.parentApp.setNextForm (None)

  def on_ok (self):
    self.parentApp.setNextForm (None)

MyApp = App ()
MyApp.run ()