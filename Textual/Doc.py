
#------------------------------------------------------------------------------------#
#---------------------------- Place Holder widget  -----------------------------------#
#------------------------------------------------------------------------------------#
#---------------------- Place holder only got one properties >> name
#---------------------- on_mount is the function to put every thing >> oncreat in npy
#---------------------- await self.view.dock () take wedgit , place and size
#------------------------------------------------------------------------------------#

# from textual.app import App
# from textual.widgets import Placeholder


# class MainApp(App):

#     async def on_mount(self) -> None:
#         await self.view.dock(Placeholder(name="header"), edge="top", size=3)
#         await self.view.dock(Placeholder(name="footer"), edge="bottom", size=3)
#         await self.view.dock(Placeholder(name="stats"), edge="left", size=40)
#         await self.view.dock(Placeholder(name="message"), edge="right", size=40)
#         await self.view.dock(Placeholder(name="grid"), edge="top")

# MainApp.run(title="Janssen")


#------------------------------------------------------------------------------------#
#---------------------------- Buttons widget  ----------------------------------------#
#------------------------------------------------------------------------------------#
#---------------------- Buttons have three properties 
#---------------------- label: the text being rendered on the button.
#---------------------- name: the name of the widget. 
#---------------------- style: label's style. It is defined using the 'foreground on background' notation. 
# --------------------- for example: style = "white on dark_blue
#------------------------------------------------------------------------------------#
# from textual.app import App
# from textual.widgets import Button


# class MainApp(App):

#     async def on_mount(self) -> None:
#         button1 = Button(label='Hello', name='button1',style = "white on dark_blue")
#         button2 = Button(label='world', name='button2', style='black on white')
#         await self.view.dock(button1, button2, edge="left")

# MainApp.run(title="Janssen")

#------------------------------------------------------------------------------------#
#---------------------------- Header widget  -----------------------------------------#
#------------------------------------------------------------------------------------#
#---------------------- Header have three properties 
#---------------------- tall: bool = True, The starting width.
#---------------------- style
#---------------------- clock: bool = True,
# ---------------------  The title of the app is written in the header
#------------------------------------------------------------------------------------#


# from textual.app import App
# from textual.widgets import Header


# class MainApp(App):

#     async def on_mount(self) -> None:
#         header = Header(clock=False,tall=False)
#         await self.view.dock(header)

# MainApp.run(title="Janssen")

#------------------------------------------------------------------------------------#
#---------------------------- Footer widget  -----------------------------------------#
#------------------------------------------------------------------------------------#
#---------------------- Footer have No properties 
#---------------------- Any Keys bind appear in the Footer
# ---------------------  can make Custom footer with diffrent text for keybind or event for mouse
#------------------------------------------------------------------------------------#
# from textual.app import App
# from textual.widgets import Footer


# class MainApp(App):

#     async def on_load(self) -> None:
#         """Bind keys here."""
#         await self.bind("q", "quit", "Quit")
#         await self.bind("t", "tweet", "Tweet")
#         await self.bind("r", "None", "Record")

#     async def on_mount(self) -> None:
#         footer = Footer()
#         await self.view.dock(footer, edge="bottom")

# MainApp.run(title="Janssen")

#------------------------------------------------------------------------------------#
#---------------------------- scroll view widget ------------------------------------#
#------------------------------------------------------------------------------------#
#---------------------- Footer have 5 properties 
#---------------------- contents
#---------------------- auto_width: bool = False,
#---------------------- name: str | None = None,
#---------------------- style: StyleType = "",
#---------------------- fluid: bool = True,
#------------------------------------------------------------------------------------#

# from textual.app import App
# from textual.widgets import ScrollView, Button

# class MainApp(App):

#     async def on_mount(self) -> None:
#         scroll_view = ScrollView(contents= Button(label='button'), auto_width=False)
#         await self.view.dock(scroll_view)

# MainApp.run(title="Janssen")

#------------------------------------------------------------------------------------#
#---------------------------- static widget -----------------------------------------#
#------------------------------------------------------------------------------------#
#---------------------- Footer have 4 properties 
#---------------------- renderable: RenderableType,
#---------------------- name: str | None = None,
#---------------------- style: StyleType = "",
#---------------------- padding: PaddingDimensions = 0,
#------------------------------------------------------------------------------------#

# from textual.app import App
# from textual.widgets import Static, Button

# class MainApp(App):

#     async def on_mount(self) -> None:
#         static1 = Static(renderable= Button(label='button1'), name='1')
#         static2 = Static(renderable= Button(label='button2'), name='2')
#         await self.view.dock(static1,static2)

# MainApp.run(title="Janssen")


#------------------------------------------------------------------------------------#
#---------------------------- Custom  widget ----------------------------------------#
#------------------------------------------------------------------------------------#

# from textual.app import App
# from textual.widget import Widget
# from textual.reactive import Reactive
# from rich.console import RenderableType
# from rich.padding import Padding
# from rich.align import Align
# from rich.text import Text

# class Letter(Widget):

#     label = Reactive("")
#     color = "white on rgb(51,51,51)"

#     def render(self) -> RenderableType:
#         return Padding(
#             Align.center(Text(text=self.label), vertical="middle"),
#             (0, 1),
#             style=self.color,
#         )

# class MainApp(App):

#     async def on_mount(self) -> None:
#         letter = Letter()
#         letter.label = "A"
#         letter.color = "white on blue"
#         await self.view.dock(letter)

# MainApp.run(title="Janssen")


#------------------------------------------------------------------------------------#
#---------------------------- Organize with views -----------------------------------#
#------------------------------------------------------------------------------------#
#----------------- In Textual, there are five types of views:
#----------------- DockView
#----------------- GridView
#----------------- WindowView
#------------------------------------------------------------------------------------#
#---------------------------- DockView ----------------------------------------------#
#------------------------------------------------------------------------------------#
#----------------- view.dock >> take the widget to view, and edge to place them
#----------------- defult is vertically
#----------------- size = char size * n
#------------------------------------------------------------------------------------#

# from textual.app import App
# from textual.widgets import Placeholder
# from textual.views import DockView

# class MainApp(App):

#     async def on_mount(self) -> None:
#         view: DockView = await self.push_view(DockView())
#         await view.dock(Placeholder(), Placeholder(), Placeholder())

# MainApp.run(title="Janssen")

#------------------------------------------------------------------------------------#
#--------------------------------- Horizontal  
#------------------------------------------------------------------------------------#

# from textual.app import App
# from textual.widgets import Placeholder
# from textual.views import DockView

# class MainApp(App):

#     async def on_mount(self) -> None:
#         view: DockView = await self.push_view(DockView())
#         await view.dock(Placeholder(), Placeholder(), Placeholder(), edge='left', size=10 )

# MainApp.run(title="Janssen")


#------------------------------------------------------------------------------------#
#---------------------------- GridView ----------------------------------------------#
#------------------------------------------------------------------------------------#

# from textual.app import App
# from textual import events
# from textual.widgets import Placeholder


# class GridView(App):
#     async def on_mount(self, event: events.Mount) -> None:
#         """Create a grid with auto-arranging cells."""

#         grid = await self.view.dock_grid()

#         grid.add_column("col", repeat=6, size=7)
#         grid.add_row("row",  repeat=6, size=7)
#         grid.set_align("stretch", "center")

#         placeholders = [Placeholder() for _ in range(36)]
#         grid.place(*placeholders)


# GridView.run(title="Grid View", log="textual.log")


#------------------------------------------------------------------------------------#
#---------------------------- WindowView --------------------------------------------#
#------------------------------------------------------------------------------------#
#--------------------A placeholder for widget.
#------------------------------------------------------------------------------------#

# from textual.app import App
# from textual.widgets import Placeholder , Header
# from textual.views import WindowView


# class MainApp(App):

#     async def on_mount(self) -> None:
#         header = Header(clock=False,tall=False)
#         await self.view.dock(header)
#         await self.view.dock(WindowView(widget=Placeholder(name='sad')), size=10)
#         await self.view.dock(WindowView(widget=Placeholder(name='happy')), size=10)

# MainApp.run(title="Janssen")


#------------------------------------------------------------------------------------#
#---------------------------- Widget Event Handler ----------------------------------#
#------------------------------------------------------------------------------------#
#-------------------- a key event handler can be simply written as:
#-------------------- def on_key(self, event):
#------------------------------------------------------------------------------------#