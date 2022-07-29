
from datetime import datetime
from logging import getLogger
from numpy import size
import rich
from rich.console import Console, ConsoleOptions, RenderableType
from rich.panel import Panel
from rich.repr import rich_repr, Result
from rich.style import StyleType
from rich.table import Table
from rich.text import TextType , Text
from textual import events
from textual.widget import Widget
from textual.reactive import watch, Reactive

#------------------------------------------------------------------#
from Messages import *


class NavBar(Widget):

    style: Reactive[StyleType] = Reactive("white on blue")
    title: Reactive[str] = Reactive("")
    mouse_down: Reactive[RenderableType] = Reactive(False)
    mouse_over: Reactive[RenderableType] = Reactive(False)
    mouse_x: Reactive[int] = Reactive(0)
    # selected_tab : Reactive[list] = Reactive([])

    #---------------------------------------------------------------------#
    #----------------------- Start Init  ---------------------------------#
    #---------------------------------------------------------------------#
    def __init__(self,*,style: StyleType = "white on dark_green",selected_tab=None,title = None,tabs=[],name) -> None:
        super().__init__()
        self.style=  style
        self.title=  title  
        self.tabs= tabs         #------ all tabs name
        self.init_flag = 0      #------ for first init only
        self.selected_tab=selected_tab  #------ the active tab
        self.mouse_x = 0
        self.name= name

    #----------------------------------------------------------------------#
    #-------------------- Handel mouse position and click -----------------#
    #----------------------------------------------------------------------#

    def on_mouse_down(self) -> None:
        self.mouse_down = True

    def on_mouse_up(self) -> None:
        self.mouse_down = False

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

    def _mouse_axis(self, event) -> int:
        x = event.x
        return x

    # async def active_tab(self)-> None:
    #     return str('gh')

    async def on_mouse_move(self, event: events.MouseMove) -> None:
        self.mouse_x = self._mouse_axis(event)

    #----------------------------------------------------------------------#
    #-------------------- Rendering and events ----------------------------#
    #----------------------------------------------------------------------#

    def render(self) -> RenderableType:
        #---------------------------------------------------------------------#
        #----------------------- First Time to load currentValues ------------#
        #----------------------- If no selected_tab > go with first one ------#
        #---------------------------------------------------------------------#
        if self.init_flag == 0:
            if  self.selected_tab in self.tabs:
                pass
            else :
                self.selected_tab = self.tabs[0]
            self.init_flag =1
        #--------------------  Creat the Table and give init values
        header_table = Table(title=self.selected_tab, box=None,min_width=self.size.width,show_edge=False,)
        #-------------------- Add All tabs name 
        #-------------------- (totalScreenSize / 2)- (chars)/2
        total_chars = 0 
        for tab_name in self.tabs:  
            total_chars += len(tab_name)        #---------- Len of each tab
        total_chars+= (len(self.tabs) -1 ) * 4  #---------- how many space
        first_tabX = int(self.size.width / 2) - int(total_chars/2)
        tab_coord= {}
        for i in range(len(self.tabs)):  ## self.tabs = ['tab1','tab2']
            tab_coord[self.tabs[i]] = {
                            'x_start':first_tabX + (4)*i + len(self.tabs[i])*i,
                            'x_end':first_tabX + (4)*i + len(self.tabs[i])*i + len(self.tabs[i]) }
        #---------------------------------------------------------------------# 
        #--------------------- perform mouse click calculation ---------------# 
        #---------------------------------------------------------------------#
        if self.mouse_down == True: 
            for i in range(len(tab_coord)) : ## tab_coord = {'tab1':{'x_start':54 ,'x_end':58},'tab2':{'x_start':62 ,'x_end':66}}
                if self.mouse_x >= tab_coord[self.tabs[i]]['x_start'] and self.mouse_x < tab_coord[self.tabs[i]]['x_end']:
                    self.selected_tab = str(self.tabs[i])
                    # self.emit(Message(self.selected_tab))
        else :
            pass

        #-------------------- selected one will be blue
        new = rich.text.Text()
        for i in self.tabs :
            if self.selected_tab == i :
                new += (Text(text=(i + '\t'),style="bold blue")) 
            else:
                new += (Text(text=(i + '\t'),style="bold red")) 
        new.justify = 'center'

        header_table.add_row(new)

        #-------------------- RenderableType and but in panel to return it
        header: RenderableType

        header = Panel(
            renderable=header_table,
             style=self.style,
             title=self.title, 
             ) 

        return header

        # return Panel(
        #     panel_group, 
        #     title="", 
        #     title_align="center", 
        #     height=4+len(self.currentValues),
        #     style=self.style or "",
        #     border_style="green" if self.mouse_over else "blue",        #-------------------- change color when mouse over it
        #     box=rich.box.HEAVY if self.has_focus else rich.box.ROUNDED, #-------------------- change box style when on_focuse
        # )





    async def on_mount(self, event: events.Mount) -> None:
        self.set_interval(1.0, callback=self.refresh)

    async def on_click(self, event: events.Click) -> None:
        # self.tall = not self.tall
        pass



