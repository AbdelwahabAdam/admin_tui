from rich.spinner import Spinner
from rich.style import StyleType
from rich.table import Table
from rich.console import RenderableType
from rich.text import Text
from typing import Optional

# ----------------------------------------------------------------------------------#


class Custom_Radio_spinner (Spinner):

    def __init__(self, name: str, widName, text: "RenderableType" = "", *, style: Optional["StyleType"] = None, sign=None, speed: float = 1) -> None:
        super().__init__(name, text, style=style, speed=speed,)
        self.sign = sign
        self.widName = widName
    # ------------------------------------------------------------------------------#
    # ------------------------------------------------------------------------------#

    def render(self, time: float) -> "RenderableType":

        if self.speed == 1:
            frame_no = self.frame_no_offset + 7
            frame = Text(
                self.frames[int(frame_no) % len(self.frames)], style='blue')
        else:
            frame_no = self.frame_no_offset
            frame = Text(
                self.frames[int(frame_no) % len(self.frames)], style='red')

        if not self.text:
            return frame
        if isinstance(self.text, (str, Text)):
            return Text.assemble(" (", str(self.sign), ")  ", self.text)
        else:
            table = Table.grid(padding=1)
            table.add_row(frame, self.text)
            return table

# ----------------------------------------------------------------------------------#

class Custom_Check_spinner (Spinner):

    def __init__(self, name: str, widName, text: "RenderableType" = "", *, style: Optional["StyleType"] = None, sign=None, speed: float = 1) -> None:
        super().__init__(name, text, style=style, speed=speed,)
        self.sign = sign
        self.widName = widName
    # ------------------------------------------------------------------------------#
    # ------------------------------------------------------------------------------#

    def render(self, time: float) -> "RenderableType":

        if self.speed == 1:
            frame_no = self.frame_no_offset + 7
            frame = Text(
                self.frames[int(frame_no) % len(self.frames)], style='blue')
        else:
            frame_no = self.frame_no_offset
            frame = Text(
                self.frames[int(frame_no) % len(self.frames)], style='red')

        if not self.text:
            return frame
        if isinstance(self.text, (str, Text)):
            return Text.assemble(" [", str(self.sign), "]  ", self.text)
        else:
            table = Table.grid(padding=1)
            table.add_row(frame, self.text)
            return table
