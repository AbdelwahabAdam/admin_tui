from rich.columns import Columns
from rich.console import Group
from rich.box import ROUNDED
from textual.reactive import Reactive
from rich.console import RenderableType
from rich.panel import Panel
from textual.widget import Widget
from textual import events
import rich.repr
from textual_inputs.events import InputOnChange, InputOnFocus, make_message_class

#--------------------------------------------------------------------------#
#------------------------- My Own Classes and Widgets ---------------------#
from Custom_spinners import *
#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#


class RadioButtons(Widget):
    mouse_down: Reactive[RenderableType] = Reactive(False)
    mouse_over: Reactive[RenderableType] = Reactive(False)

    
    def __init__(self, sign, name, title: str, data=[]):
        super().__init__(title)
        self.title = title
        self.sign = sign
        self.data = data
        self.name = name
        self.mouse_y = 0
        self.mouse_x =0
        self.init_flag = 0
        self.currentValues = {}
        self.on_focuse = False

    # def has_focus(self) -> bool:
    #     """Produces True if widget is focused"""
    #     return self.mouse_down

    
    def on_mouse_down(self) -> None:
        self.mouse_down = True
        self.on_focuse = True

    def on_mouse_up(self) -> None:
        self.mouse_down = False

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False


    def _mouse_axisY(self, event) -> int:
        y = event.y
        return y

    def _mouse_axisX(self, event) -> int:
        x = event.x
        return x
    async def on_mouse_move(self, event: events.MouseMove) -> None:

        self.mouse_y = self._mouse_axisY(event)
        self.mouse_x = self._mouse_axisX(event)


    def render(self) -> RenderableType:
        #---------------------------------------------------------------------#
        #----------------------- First Time to load currentValues ------------#
        #---------------------------------------------------------------------#
        if self.init_flag == 0:
            for i in range(len(self.data)) :
                self.currentValues[i] = [self.data[i][0],'0']
                self.init_flag = 1
            self.currentValues[0][1] = '1'
        #---------------------------------------------------------------------#
        #----------------------- Load what is selected -----------------------#
        #---------------------------------------------------------------------#
        for idex in range(len(self.currentValues)):
            if self.currentValues[idex][1] == '1' :
                select = self.currentValues[idex][0]
                break
            else :
                select='None  '
        if len(select) < 6:
            select = select + ' '*(6-len(select))
        #---------------------------------------------------------------------#
        #----------------------- Creating the Widget and render it -----------#
        #---------------------------------------------------------------------#

        #-------------------- Heading and Title -------------------------------#

        table = Table(title='', box=None)
        # table.add_column(self.title+': ' +str(select), style="cyan", no_wrap=True)
        table.add_column(str(self.size.width)+'y: ' +str(self.mouse_y)+'x: ' +str(self.mouse_x), style="cyan", no_wrap=True)

        #--------------------  Selection based on Mouse.y click ----------------#

        for widget_len in range(len(list(self.currentValues.keys()))): 
            if self.mouse_down == True:                                                                           #--------------------  If mouse clicked
                if int(self.mouse_y) == 2 + list(self.currentValues.keys())[widget_len]  :                  #--------------------  If mouse.y in limit of any choice
                    self.currentValues[widget_len][1] = '1'
                    
                    table.add_row('', Custom_Radio_spinner(
                        name='toggle7', text=self.currentValues[widget_len][0], speed=1, sign=self.sign, widName=self.currentValues[widget_len][0]), style="green")
                    

                elif int(self.mouse_y) < self.size.height - list(self.currentValues.keys())[widget_len]  :  #--------------------  If mouse.y is not in limit of any choice
                    self.currentValues[widget_len][1] = '0'
                    table.add_row('', Custom_Radio_spinner(
                        name='toggle7', text=self.currentValues[widget_len][0], speed=1, sign=' ', widName=self.currentValues[widget_len][0]), style="green")
                else :                                                                                      #--------------------  If mouse clicked outside all choices
                    self.mouse_down = True
            
            else :                                                                                          #--------------------  If mouse not clicked
                sign_now= self.sign if self.currentValues[widget_len][1] == '1' else ' '
                table.add_row('', Custom_Radio_spinner(
                        name='toggle7', text=self.currentValues[widget_len][0], speed=1, sign=sign_now, widName=self.currentValues[widget_len][0]), style="green")
        #----------------------------------------------------------------------#
        #-------------------- Rendering and events ----------------------------#
        #----------------------------------------------------------------------#

        user_renderables = [table]
        panel_group = Columns(user_renderables)
        return Panel(
            panel_group, 
            title="", 
            title_align="center", 
            height=4+len(self.currentValues),
            style=self.style or "",
            border_style="green" if self.mouse_over else "blue"  ,        #-------------------- change color when mouse over it
            box=rich.box.HEAVY if self.mouse_down else rich.box.ROUNDED, #-------------------- change box style when on_focuse
        ) #"white" if self.has_focus else  "green" if self.border == 'True' else "blue",
# ----------------------------------------------------------------------------------#


