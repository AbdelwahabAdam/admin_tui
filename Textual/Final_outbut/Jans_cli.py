
from textual.app import App
from textual.widgets import Placeholder
#--------------------------------------------------------------------------#
#------------------------- My Own Classes and Widgets ---------------------#
#--------------------------------------------------------------------------#
from RadioButtons import *
from CheckBox import *
from CustomTextInput import *
#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
from textual.widgets import Header, Footer
from typing import Type
from textual.driver import Driver


help_text_dict = {
    'displayName': ("Name of the user suitable for display to end-users"),
    'clientSecret': ("The client secret. The client MAY omit the parameter if the client secret is an empty string"),
    'redirectUris': ("Redirection URI values used by the Client. One of these registered Redirection URI values must exactly match the redirect_uri parameter value used in each Authorization Request"),
    'responseTypes': ("A list of the OAuth 2.0 response_type values that the Client is declaring that it will restrict itself to using. If omitted, the default is that the Client will use only the code Response Type. Allowed values are code, token, id_token"),
    'applicationType': ("Kind of the application. The default, if omitted, is web. The defined values are native or web. Web Clients using the OAuth Implicit Grant Type must only register URLs using the HTTPS scheme as redirect_uris, they must not use localhost as the hostname. Native Clients must only register redirect_uris using custom URI schemes or URLs using the http scheme with localhost as the hostname"),
    'helper': ("To guide you through the fields"),

}

class Jans_cli(App):

    def __init__(self,widgetList=[], screen: bool = True, driver_class: Type[Driver] | None = None, log: str = "", log_verbosity: int = 1, title: str = "Textual Application"):
        super().__init__(screen, driver_class, log, log_verbosity, title)
        self.widgetList = widgetList

    async def on_mount(self) -> None:
        #------------------------------------------------------------------#
        #------------------------ Define Grid and positions ---------------#
        #------------------------------------------------------------------#

        grid = await self.view.dock_grid(edge="left", name="left")

        grid.add_column(fraction=2, name="left", size=60)
        grid.add_column(fraction=1, name="center")
        grid.add_column(fraction=1, name="right")

        grid.add_row(fraction=1, name="1", size=3)
        grid.add_row(fraction=2, name="2", size=3)
        grid.add_row(fraction=1, name="3", size=7)

        grid.add_row(fraction=1, name="4", size=6) ## RadioButtons
        grid.add_row(fraction=1, name="5", size=7) ## check box


        grid.add_row(fraction=1, name="6", size=6) 
        # grid.add_row(fraction=1, name="7", size=5)

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
            name="clientSecret", title="Client Secret: ")
        self.redirectUris = CustomTextInput(
            name="redirectUris", title="Redirect Uris: ", placeholder='long')
        self.myRadioButton = RadioButtons(title='Aplication Type', sign='*', name='AplicationType',
                               data=[('web', 'web'), ('native', 'native')])
        
        myCheckBox = self.myCheckBox =CheckBox(title='Response Types:', sign='*', name='ResponseTypes',
                               data=('code', 'token', 'id_token'))  # TODO >> selection   

        #------------------------------------------------------------------#
        #------------------------ Appending Widgets -----------------------#
        #------------------------ This List for navigation order ----------#
        #------------------------------------------------------------------#
        self.widgetList.append(self.displayName)
        self.widgetList.append(self.clientSecret)
        self.widgetList.append(self.redirectUris)
        self.widgetList.append(self.myRadioButton)
        self.widgetList.append(self.myCheckBox)
        #------------------------------------------------------------------#
        #------------------------ Place widgets to grid -------------------#
        #------------------------------------------------------------------#
        grid.place(
            area1=self.displayName,
            area2=self.clientSecret,
            area3=self.redirectUris,
            area4=self.myRadioButton,
            area5=self.myCheckBox,
            area6= Footer()
        )
        


    async def on_load(self) -> None:
        """Sent before going in to application mode."""

        await self.bind("ctrl+i", "navigate", "TAB")

    # async def on_key(self, event: events.Key) -> None:  ## print all keys on textinput
    #     await self.press(event.key)
    #     self.redirectUris.value = str(event.key)

    async def action_navigate(self) -> None: ## work as key
        for i in range(len(self.widgetList)) :
            if self.widgetList[i].name not in ['AplicationType','ResponseTypes']:
                if self.widgetList[i].has_focus:

                #     self.widgetList[i].value = 'Focuse here'
                # else :
                #     self.widgetList[i].value = ''
                    try :
                    # if i < len((self.widgetList)) +1 :
                    # self.redirectUris.value = str((self.widgetList[i]))
                        await self.widgetList[i+1].focus()
                    except:
                        pass




Jans_cli.run(title="Grid Test", log="textual.log")
