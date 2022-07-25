
from textual.app import App
from textual.widgets import Placeholder
#--------------------------------------------------------------------------#
#------------------------- My Own Classes and Widgets ---------------------#
#--------------------------------------------------------------------------#
from RadioButtons import *
from CustomTextInput import *
#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#


help_text_dict = {
    'displayName': ("Name of the user suitable for display to end-users"),
    'clientSecret': ("The client secret. The client MAY omit the parameter if the client secret is an empty string"),
    'redirectUris': ("Redirection URI values used by the Client. One of these registered Redirection URI values must exactly match the redirect_uri parameter value used in each Authorization Request"),
    'responseTypes': ("A list of the OAuth 2.0 response_type values that the Client is declaring that it will restrict itself to using. If omitted, the default is that the Client will use only the code Response Type. Allowed values are code, token, id_token"),
    'applicationType': ("Kind of the application. The default, if omitted, is web. The defined values are native or web. Web Clients using the OAuth Implicit Grant Type must only register URLs using the HTTPS scheme as redirect_uris, they must not use localhost as the hostname. Native Clients must only register redirect_uris using custom URI schemes or URLs using the http scheme with localhost as the hostname"),
    'helper': ("To guide you through the fields"),

}


class CutomPlaceholder (Placeholder):

    def _mouse_axis(self, event) -> int:
        y = event.y
        return y

    async def on_mouse_down(self, event: events.MouseDown) -> None:
        mouse_axis = self._mouse_axis(event)
        self.name = str(mouse_axis) + "value"

    async def on_mouse_move(self, event: events.MouseMove) -> None:
        mouse_axis = self._mouse_axis(event)
        self.name = str(mouse_axis) + "value"


class Jans_cli(App):

    async def on_mount(self) -> None:
        #------------------------------------------------------------------#
        #------------------------ Define Grid and positions ---------------#
        #------------------------------------------------------------------#

        grid = await self.view.dock_grid(edge="left", name="left")

        grid.add_column(fraction=2, name="left", size=50)
        grid.add_column(fraction=1, name="center")
        grid.add_column(fraction=1, name="right")

        grid.add_row(fraction=1, name="1", size=3)
        grid.add_row(fraction=2, name="2", size=3)
        grid.add_row(fraction=1, name="3", size=7)
        grid.add_row(fraction=1, name="4", size=1)
        grid.add_row(fraction=1, name="5", size=10)
        grid.add_row(fraction=1, name="6", size=5)
        grid.add_row(fraction=1, name="7", size=5)

        grid.add_areas(
            area1="left,1",
            area2="left,2",
            area3="left,3",
            area4="left,4",
            area5="left,5",
            area6="left,6",
            area7="Center,3",
        )
        #------------------------------------------------------------------#
        #------------------------ Define Widgets --------------------------#
        #------------------------------------------------------------------#
        self.displayName = CustomTextInput(
            name="displayName", title="Display Name: ")
        self.clientSecret = CustomTextInput(
            name="clientSecret", title="Client Secret: ",)
        self.redirectUris = CustomTextInput(
            name="redirectUris", title="Redirect Uris: ", placeholder='long')
        # self.helper = CustomTextInput(
        #     name="helper", placeholder='helper', title="helper",)
        #------------------------------------------------------------------#
        #------------------------ Place widgets to grid -------------------#
        #------------------------------------------------------------------#
        grid.place(
            area1=self.displayName,
            area2=self.clientSecret,
            area3=self.redirectUris,
            area5=RadioButtons(title='Aplication Type', sign='*', name='web',
                               data=[('web', 'web'), ('native', 'native'), ]),  # TODO >> selection
        )


Jans_cli.run(title="Grid Test", log="textual.log")
