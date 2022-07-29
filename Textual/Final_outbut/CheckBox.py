from rich.columns import Columns
from rich.console import Group
from rich.box import ROUNDED
from textual.reactive import Reactive
from rich.console import RenderableType
from rich.panel import Panel
from textual.widget import Widget
from textual import events
#--------------------------------------------------------------------------#
#------------------------- My Own Classes and Widgets ---------------------#
from Custom_spinners import *
#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#


class CheckBox(Widget):  # NOT DONE >> DONT TRY YET
    mouse_down: Reactive[RenderableType] = Reactive(False)
    mouse_over: Reactive[RenderableType] = Reactive(False)

    def __init__(self, sign, name, title: str, data=[], mouse_y=0):
        super().__init__(title)
        self.title = title
        self.sign = sign
        self.data = data
        self.name = name
        self.mouse_y = mouse_y
        self.init_flag = 0
        self.currentValues = {}


    def has_focus(self) -> bool:
        """Produces True if widget is focused"""
        return False #self.mouse_down



    def on_mouse_down(self) -> None:
        self.mouse_down = True

    def on_mouse_up(self) -> None:
        self.mouse_down = False

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

    def _mouse_axis(self, event) -> int:
        y = event.y
        return y

    async def on_mouse_move(self, event: events.MouseMove) -> None:

        self.mouse_y = self._mouse_axis(event)

    def render(self) -> RenderableType:
        if self.init_flag == 0:
            for item in range(len(self.data)):
                self.currentValues[item] = [self.data[item] , '0']
                self.init_flag = 1
       
        table = Table(title='', box=None)
        table.add_column(self.title, style="cyan", no_wrap=False)

        for widget_len in range(len(list(self.currentValues.keys()))):
            if self.mouse_down == True:
                if int(self.mouse_y) == 2 + list(self.currentValues.keys())[widget_len]  :   ## self.currentValues[widget_len] =['web', '0']
                    
                    if self.currentValues[widget_len][1] == '1':
                        self.currentValues[widget_len][1] = '0'
                    else :
                        self.currentValues[widget_len][1] = '1'
                    
                    table.add_row('', Custom_Radio_spinner(
                        name='toggle7', text=self.currentValues[widget_len][0], speed=1, sign=self.sign, widName=self.currentValues[widget_len][0]), style="green")
                    self.mouse_down = False
                else :
                    sign_now= self.sign if self.currentValues[widget_len][1] == '1' else ' '
                    table.add_row('', Custom_Check_spinner(
                            name='toggle7', text=self.currentValues[widget_len][0], speed=1, sign=sign_now, widName=self.currentValues[widget_len][0]), style="green")

                
            else :
                sign_now= self.sign if self.currentValues[widget_len][1] == '1' else ' '
                table.add_row('', Custom_Check_spinner(
                        name='toggle7', text=self.currentValues[widget_len][0], speed=1, sign=sign_now, widName=self.currentValues[widget_len][0]), style="green")


        user_renderables = [table]
        panel_group = Columns(user_renderables)
        return Panel(
            panel_group,
            title="",
            title_align="center",
            height=4+len(self.currentValues),
            style=self.style or "",
            border_style="green" if self.mouse_over else "blue",
            box=ROUNDED,
        )