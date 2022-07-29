from textual import events
from textual_inputs import TextInput
import rich.repr
from rich.console import RenderableType
from rich.text import Text
from rich.panel import Panel
from textual.message import Message


help_text_dict = {
    'displayName': ("Name of the user suitable for display to end-users"),
    'clientSecret': ("The client secret. The client MAY omit the parameter if the client secret is an empty string"),
    'redirectUris': ("Redirection URI values used by the Client. One of these registered Redirection URI values must exactly match the redirect_uri parameter value used in each Authorization Request"),
    'responseTypes': ("A list of the OAuth 2.0 response_type values that the Client is declaring that it will restrict itself to using. If omitted, the default is that the Client will use only the code Response Type. Allowed values are code, token, id_token"),
    'applicationType': ("Kind of the application. The default, if omitted, is web. The defined values are native or web. Web Clients using the OAuth Implicit Grant Type must only register URLs using the HTTPS scheme as redirect_uris, they must not use localhost as the hostname. Native Clients must only register redirect_uris using custom URI schemes or URLs using the http scheme with localhost as the hostname"),
    'helper': ("To guide you through the fields"),

}


class CustomTextInput (TextInput):

    # def _key_printable(self, event: events.Key):
    #     """Handle all printable keys"""
    #     if self.name == 'redirectUris':
    #         # self.value = str(event.key)
    #         if event.key == '*' : ### TODO Enter is not defined here!! 
    #             self.value = (
    #                 self.value[: self._cursor_position]
    #                 + 'k'
    #                 + self.value[self._cursor_position:]
    #             )
    #         else:
    #             self.value = (
    #                 self.value[: self._cursor_position]
    #                 + event.key
    #                 + self.value[self._cursor_position:]
    #             )
    #     else:
    #         # self.value = str(event.key)
    #         self.value = (
    #             self.value[: self._cursor_position]
    #             + event.key
    #             + self.value[self._cursor_position:]
    #         )

    #     if not self._cursor_position > len(self.value):
    #         self._cursor_position += 1
    #         self._update_offset_right()

    async def on_enter(self) -> None:
        self.border = 'True'
        self.wid_name = self.name
        await self.emit(ValueBarChange(self))
        
    async def on_leave(self) -> None:
        self.border = 'False'
        await self.emit(ValueBarChange(self))

    def _cursor_enter(self):
        """Handle key press enter"""
        # self.value += str(self._cursor_position)\
        if self.placeholder == 'long' :
            self.value = (self.value[: self._cursor_position]+ '\n')
            self._cursor_position +=1
                                                                                                
    async def on_key(self, event: events.Key) -> None:

        BACKSPACE = "ctrl+h"
        if event.key == "left":
            self._cursor_left()
        elif event.key == "right":
            self._cursor_right()
        elif event.key == "home":
            self._cursor_home()
        elif event.key == "end":
            self._cursor_end()
        elif event.key == BACKSPACE:
            self._key_backspace()
            await self._emit_on_change(event)
        elif event.key == "delete":
            self._key_delete()
            await self._emit_on_change(event)
            #----------------------------- ENTER KEY TRY -----------------#
        elif event.key == "enter":
            self._cursor_enter()
            #----------------------------- ENTER KEY TRY -----------------#
    def render(self) -> RenderableType:
        """
        Produce a Panel object containing placeholder text or value
        and cursor.
        """
        if self.has_focus:
            segments = self._render_text_with_cursor()
        else:
            if len(self.value) == 0:
                if self.title:
                    segments = [self.title]
                else:
                    segments = ''
            else:
                segments = [self._modify_text(self.value)]
        text = Text.assemble(*segments)

        if (
            self.title

            and len(self.value) == 0
            and not self.has_focus
        ):
            title = ""
        else:
            title = self.title

        return Panel(
            text,
            title=title,
            title_align="left",
            height=7 if self.placeholder == 'long' else 3,
            width=80,
            style=self.style or "",
            border_style="white" if self.has_focus else  "green" if self.border == 'True' else "blue",
            box=rich.box.HEAVY if self.has_focus else rich.box.ROUNDED,

        )


# ----------------------------------------------------------------------------------#


class ValueBarChange(Message):
    def __init__(self, sender: CustomTextInput) -> None:
        super().__init__(sender)

        ### Can View Message on each object
        # self.value = sender.value  # TODO make helper only change

        # if sender.border == 'True':
        #     sender.value = help_text_dict[sender.name]
        # else:
        #     sender.value = ''





