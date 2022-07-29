from time import sleep

from rich.columns import Columns
from rich.panel import Panel
from rich.live import Live
from rich.text import Text
from rich.spinner import Spinner
from rich.console import RenderableType
from rich.text import Text
from rich.panel import Panel
from typing import  Optional
from rich.style import StyleType
from rich.table import Table
from rich.columns import Columns
from rich.console import Group
from textual.reactive import Reactive
from textual.app import App
from textual.widgets import Placeholder
from textual_inputs import TextInput, IntegerInput
from textual.reactive import Reactive
import rich.repr
from rich.console import RenderableType
from rich.text import Text
from rich.panel import Panel
from rich.style import Style
from typing import TYPE_CHECKING, Any, List, Optional, Tuple, Union
from textual_inputs.events import InputOnChange, InputOnFocus, make_message_class
from textual.widget import Widget
from textual.driver import Driver
from typing import Any, Callable, ClassVar, Type, TypeVar
from textual import events
from rich.console import Console
from rich.table import Table
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.text import Text
from rich.spinner import Spinner, SPINNERS
from rich.console import Group
from rich.style import StyleType
from rich.box import ROUNDED
from rich import box
# ----------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------#
class custom_spinner (Spinner):

    # sign: Reactive[RenderableType] = Reactive("")

    def __init__(self, name: str, text: "RenderableType" = "", *, style: Optional["StyleType"] = None, sign = None, speed: float = 1) -> None:
        super().__init__(name, text, style=style,speed=speed,)
        self.sign = sign
    # ------------------------------------------------------------------------------#
    # ------------------------------------------------------------------------------#

    def render(self, time: float) -> "RenderableType":
        
        if self.speed ==1 :
            frame_no =  self.frame_no_offset + 7
            frame = Text(
            self.frames[int(frame_no) % len(self.frames)], style='blue' )
        else :
            frame_no =  self.frame_no_offset 
            frame = Text(
            self.frames[int(frame_no) % len(self.frames)], style='red' )

        if not self.text:
            return frame
        if isinstance(self.text, (str, Text)):
            return Text.assemble(self.text, " (", str(self.sign) ," )")
        else:
            table = Table.grid(padding=1)
            table.add_row(frame, self.text)
            return table

# ----------------
class RadioButtons(Widget):

    choices: Reactive[RenderableType] = Reactive("")
    mouse_down: Reactive[RenderableType] = Reactive("")
    mouse_over: Reactive[RenderableType] = Reactive(False)

    def __init__(self,sign,data, title: str):
        super().__init__(title)
        self.title = title
        self.sign = sign
        self.data= data

    def on_mouse_down(self) -> None:
        self.mouse_down = True
        if self.choices == 0:
            self.choices = 1
        else :
            self.choices = 0


    def on_mouse_up(self) -> None:
        self.mouse_down = False

        

    def on_enter(self) -> None:
        self.mouse_over = True
        
    def on_leave(self) -> None:
        self.mouse_over = False
        

    def render(self) -> RenderableType:
        if self.choices ==0:
            panel_group = Group(
                # Panel(self.title,box=box.MINIMAL),
                custom_spinner('toggle7', text=self.data,speed=1,sign=' ' ),
            )
        else:
            panel_group = Group(
                # Panel(self.title,box=box.MINIMAL,),
                custom_spinner('toggle7', text=self.data,speed=1,sign=self.sign ),
            )
        # all_spinners = Columns(
        #     [
        #         Panel("RadioButtons",),
        #         custom_spinner('toggle7', text='Choice 1',speed=1,sign='✓'),

        #     ])
        return Panel(
            panel_group,
            title="",
            title_align="center",
            height=3 , # if self.title == '' else 8 
            style=self.style or "",
            border_style=Style(color="blue"),
            box=ROUNDED,

        )



# ----------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------#

all_spinners = Columns(
    [
    RadioButtons(title='hello',sign='✓',data='code'),
    RadioButtons(title='',sign='✓',data='Token'),
    RadioButtons(title='',sign='✓',data='ID-Token')

    ],
        column_first=True,
        expand=True,
    )

with Live(
    Panel(all_spinners, title="RadioButtons", border_style="blue",width=20),
    refresh_per_second=20,
) as live:
    while True:
        sleep(0.1)



# all_spinners = Columns(
#     [
#         custom_spinner('toggle7', text='RadioButtons',speed=1)
        
#     ],
#     column_first=True,
#     expand=True,
# )