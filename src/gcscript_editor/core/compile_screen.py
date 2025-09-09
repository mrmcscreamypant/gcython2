from textual.app import ComposeResult
from textual.binding import Binding
from textual.screen import Screen
from textual.widgets import Footer, Header


class CompileScreen(Screen):

    BINDINGS = [
        Binding("escape", "leave_compiler", "Back to editor")
    ]

    def compose(self) -> ComposeResult:
        yield Header(
            show_clock=True,
            name="GCScript Compiler",
            icon="📜"
        )
        yield Footer()

    async def action_leave_compiler(self):
        await self.app.pop_screen()