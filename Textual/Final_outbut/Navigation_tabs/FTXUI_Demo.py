
from textual.app import App
from textual.widgets import Placeholder
#--------------------------------------------------------------------------#
#------------------------- My Own Classes and Widgets ---------------------#
#--------------------------------------------------------------------------#
from Nav_bar import *
from Messages import *

#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
from textual.widgets import Header, Footer
from textual.binding import NoBinding


class Jans_cli(App):

    async def on_mount(self) -> None:
        #------------------------------------------------------------------#
        #------------------------ Define Grid and positions ---------------#
        #------------------------------------------------------------------#

        grid = await self.view.dock_grid(edge="left", name="left")

        grid.add_column(fraction=2, name="left")

        grid.add_row(fraction=1, name="1", size=5)
        grid.add_row(fraction=2, name="2")
        grid.add_row(fraction=1, name="3")

        grid.add_areas(
            area1="left,1",
            area2="left,2",
            area3="left,3",
        )
        #------------------------------------------------------------------#
        #------------------------ Define Widgets --------------------------#
        #------------------------------------------------------------------#
        self.nav_bar =NavBar(title='Nav Title',tabs=['tab1','tab2'],name = 'navbar')
        self.content = Placeholder()
        # self.emit(Message(self.content))


        grid.place(
            area1=self.nav_bar,
            area2=self.content,
            area3= Footer()
        )
        

    async def on_load(self) -> None:
        """Sent before going in to application mode."""

        await self.bind("q", "quit", "Quit : This is Footer")
        await self.bind("left", "left", "left : left")
        await self.bind("rigt", "rigt", "rigt : rigt")


    async def action_quit(self) -> None:
        await self.shutdown()


    async def action_left(self) -> None:
        self.nav_bar.selected_tab = 'tab1'
    async def action_rigt(self) -> None:
        self.nav_bar.selected_tab = 'tab2'


    # async def press(self, key: str) -> bool:
    #     """Handle a key press.

    #     Args:
    #         key (str): A key

    #     Returns:
    #         bool: True if the key was handled by a binding, otherwise False
    #     """
    #     if key == 'left':
    #         self.nav_bar.selected_tab = 'tab1'
    #     elif key == 'right':
    #         self.nav_bar.selected_tab = 'tab2'

    #     try:
    #         binding = self.bindings.get_key(key)
    #     except NoBinding:
    #         return False
    #     else:
    #         await self.action(binding.action)
    #     return True

Jans_cli.run(title="Grid Test", log="textual.log")




