from textual.app import App
from textual.widget import Widget
from rich.panel import Panel


class MyWidget(Widget):
    def render(self):
        my_renderable = Panel("press q to quit")
        return my_renderable


class MyApp(App):
    async def on_mount(self) -> None:
        await self.view.dock(MyWidget(), edge="top")
        await self.bind("q", "quit")


if __name__ == "__main__":
    MyApp.run(log="textual.log")