from rich.align import Align
from rich.box import DOUBLE
from rich.console import RenderableType
from rich.panel import Panel
from rich.style import Style
from rich.text import Text
from textual import events
from textual.app import App
from textual.reactive import Reactive
from textual.views import GridView
from textual.widget import Widget
from textual.widgets import Button, ButtonPressed ,Header ,Footer


class InputText(Widget):

    title: Reactive[RenderableType] = Reactive("")
    content: Reactive[RenderableType] = Reactive("")
    mouse_over: Reactive[RenderableType] = Reactive(False)

    def __init__(self, title: str):
        super().__init__(title)
        self.title = title

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

    def on_key(self, event: events.Key) -> None:
        if self.mouse_over == True:
            if event.key == "ctrl+h":
                self.content = self.content[:-1]
            else:
                self.content += event.key

    def validate_title(self, value) -> None:
        try:
            return value.lower()
        except (AttributeError, TypeError):
            raise AssertionError("title attribute should be a string.")

    def render(self) -> RenderableType:
        renderable = None
        if self.title.lower() == "clientsecret":
            self.content = self.content.replace('enter','')
            renderable = "".join(map(lambda char: "*", self.content))
        elif self.title.lower() == "redirecturls":
            if 'enter' in self.content :
                self.content = self.content.replace('enter','\n')
            renderable = Align.left(Text(self.content, style="bold"))
        else:
            self.content = self.content.replace('enter','')
            renderable = Align.left(Text(self.content, style="bold"))
        return Panel(
            renderable,
            title="",
            title_align="center",
            height=4,
            style="bold white on rgb(50,57,50)",
            border_style=Style(color="green"),
            box=DOUBLE,
        )


class wedGrid(GridView):


    displayName: Reactive[RenderableType] = Reactive("")
    clientSecret: Reactive[RenderableType] = Reactive("")    
    redirectUrls: Reactive[RenderableType] = Reactive("")

    async def on_mount(self) -> None:
        # define input fields
        self.displayName = InputText("displayName")
        self.clientSecret = InputText("clientSecret")
        self.redirectUrls = InputText("redirectUrls")

        self.grid.set_align("center", "center")
        self.grid.set_gap(3, 3)
        # Create rows / columns / areas
        self.grid.add_column("column", repeat=2, size=40)
        self.grid.add_row("row", repeat=4, size=4)
        # Place out widgets in to the layout
        label_style = "bold white on rgb(60,60,60)"
        displayName_label = Button(label="displayName", name="displayName_label", style=label_style)
        clientSecret_label = Button(label="clientSecret", name="clientSecret_label", style=label_style)
        redirectUrls_label = Button(label="redirectUrls", name="redirectUrls_label", style=label_style)

        self.grid.add_widget(displayName_label)
        self.grid.add_widget(self.displayName)
        self.grid.add_widget(clientSecret_label)
        self.grid.add_widget(self.clientSecret)
        self.grid.add_widget(redirectUrls_label)
        self.grid.add_widget(self.redirectUrls)
        results_label = Button(label="", name="results_label_label", style=label_style)

        self.grid.add_widget(Button(label="Submit", name="Submit", style="bold red on white"))
        self.grid.add_widget(results_label)


class MainApp(App):
    displayName: Reactive[RenderableType] = Reactive("")
    clientSecret: Reactive[RenderableType] = Reactive("")
    redirectUrls: Reactive[RenderableType] = Reactive("")

    async def handle_button_pressed(self, message: ButtonPressed) -> None:
        """A message sent by the submit button"""
        assert isinstance(message.sender, Button)
        button_name = message.sender.name
        if button_name == "Submit":
            self.displayName = self.wedGrid.displayName.content
            self.clientSecret = self.wedGrid.clientSecret.content
            self.redirectUrls = self.wedGrid.redirectUrls.content

    async def on_mount(self) -> None:
        header = Header(clock=True,tall=False)
        footer = Footer()
        self.wedGrid = wedGrid()
        await self.view.dock(header,self.wedGrid,footer)


if __name__ == "__main__":
    MainApp.run(title="jans-clint-ui",log="textual.log")