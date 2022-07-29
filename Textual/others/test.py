import sys
from textual.widgets import Placeholder
from textual.widget import Widget
from textual.events import Message
from textual.app import App
from textual import events
from textual_inputs import TextInput, IntegerInput
from ck_widgets.widgets import ListViewUo
from rich.style import Style
from typing import Any, Callable, ClassVar, Type, TypeVar


# class CustomTextbox (TextInput):


from typing import TYPE_CHECKING

from rich.panel import Panel
from rich.style import Style
from rich.text import Text
from textual import events
from textual.app import App
from rich.console import RenderableType
from rich.align import Align
from rich.box import DOUBLE


if TYPE_CHECKING:
    from textual.message import Message

help_text_dict = {
    'displayName': ("Name of the user suitable for display to end-users"),
    'clientSecret': ("The client secret. The client MAY omit the parameter if the client secret is an empty string"),
    'redirectUris': ("Redirection URI values used by the Client. One of these registered Redirection URI values must exactly match the redirect_uri parameter value used in each Authorization Request"),
    'responseTypes': ("A list of the OAuth 2.0 response_type values that the Client is declaring that it will restrict itself to using. If omitted, the default is that the Client will use only the code Response Type. Allowed values are code, token, id_token"),
    'applicationType': ("Kind of the application. The default, if omitted, is web. The defined values are native or web. Web Clients using the OAuth Implicit Grant Type must only register URLs using the HTTPS scheme as redirect_uris, they must not use localhost as the hostname. Native Clients must only register redirect_uris using custom URI schemes or URLs using the http scheme with localhost as the hostname"),
    }
#----------------------------------------------------------------------#  
#---------------------- Custom TextInput ------------------------------#  
#----------------------------------------------------------------------#  
# class InputText(TextInput):
#     # def on_click(self) -> None:
#     #     sys.exit(0)

#     def render(self) -> RenderableType:
#         renderable = Align.left(Text("", style="bold"))
#         return Panel(
#             renderable,
#             title="input_text",
#             title_align="center",
#             height=3,
#             style="bold white on rgb(50,57,50)",
#             border_style=Style(color="blue"),
#             box=DOUBLE,
#         )
#----------------------------------------------------------------------#  
#----------------------------------------------------------------------#  
#----------------------------------------------------------------------#  

class TestListView(App):

    async def on_mount(self, event: events.Mount) -> None:   
        self.displayName=TextInput(name="displayName",placeholder=help_text_dict['displayName'],title="Display Name: ")
        self.clientSecret=TextInput(name="clientSecret",placeholder=help_text_dict['clientSecret'],title="Client Secret: ",) 
        self.redirectUris=TextInput(name="redirectUris",placeholder=help_text_dict['redirectUris'],title="Redirect Uris: ",)
        self.helper=TextInput(name="helper",placeholder='helper',title="helper",)


        await self.view.dock(ListViewUo([self.displayName,self.clientSecret,self.redirectUris,self.helper]))

    

    # async def on_event(self, event: events.Event) -> None:
    #     self.helper.value='bebebeb'




    def handle_helper (self):
        self.helper.value = "focused"
        
    # displayName.on_focus_handler_name=handle_help()
    # clientSecret.on_focus_handler_name=handle_help()
    # redirectUris.on_focus_handler_name=handle_help()
    








    

if __name__ == "__main__":
    TestListView.run()