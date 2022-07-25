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


class RadioButtons(Widget):

    choices: Reactive[RenderableType] = Reactive("")
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

    def on_mouse_down(self) -> None:
        self.mouse_down = True
        self.choices = 1

    def on_mouse_up(self) -> None:
        self.mouse_down = False
        self.choices = 0

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
        table = Table(title='', box=None)
        table.add_column(self.title, style="cyan", no_wrap=True)

        for item in self.data:  # TODO >> click coordinates adjust the selected one
            if self.choices == 1:
                if int(str(self.mouse_y)) <= 2:
                    table.add_row('', Custom_Radio_spinner(
                        name='toggle7', text=item[0], speed=1, sign=self.sign, widName=item[1]), style="green")
                else:
                    table.add_row('', Custom_Radio_spinner(
                        name='toggle7', text=item[0], speed=1, sign=' ', widName=item[1]), style="green")
            else:
                table.add_row('', Custom_Radio_spinner(
                    name='toggle7', text=item[0], speed=1, sign=' ', widName=item[1]), style="green")
                pass

        user_renderables = [table]
        panel_group = Columns(user_renderables)
        return Panel(
            panel_group,
            title="",
            title_align="center",
            height=4+len(self.data),
            style=self.style or "",
            border_style="green" if self.mouse_over else "blue",
            box=ROUNDED,
        )
# ----------------------------------------------------------------------------------#


class CheckBox(Widget):  # NOT DONE >> DONT TRY YET

    # choices: Reactive[RenderableType] = Reactive([])
    # mouse_down: Reactive[RenderableType] = Reactive(False)
    mouse_over: Reactive[RenderableType] = Reactive(False)

    def __init__(self, name, sign, data, title: str):
        super().__init__(title)
        self.title = title
        self.sign = sign
        self.data = data
        self.name = name

    def on_mouse_down(self) -> None:
        self.mouse_down = True

    def on_mouse_up(self) -> None:
        self.mouse_down = False

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

    def render(self) -> RenderableType:
        panel_group = Group(
            Custom_Radio_spinner('toggle7', text=str(
                self.data[0]), speed=1, sign=self.sign, widName=self.name),
            Custom_Radio_spinner('toggle7', text=str(
                self.data[1]), speed=1, sign=self.sign, widName=self.name),
            Custom_Radio_spinner('toggle7', text=str(
                self.data[2]), speed=1, sign=self.sign, widName=self.name),
        )

        return Panel(
            panel_group,
            title="",
            title_align="center",

            style=self.style or "",
            border_style="green" if self.mouse_over else "blue",
            box=ROUNDED,

        )
# ----------------------------------------------------------------------------------#
