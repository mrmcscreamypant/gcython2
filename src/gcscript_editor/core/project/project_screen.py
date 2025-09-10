from textual.screen import Screen
from textual import work
from textual.app import ComposeResult
from textual.widgets import Placeholder, Header, Footer, Input
from textual.containers import VerticalScroll

from gcscript_editor.core.prompt import Prompt


class ProjectScreen(Screen):
    CSS_PATH = "project_screen.tcss"
    
    def compose(self) -> ComposeResult:
        yield Header(
            show_clock=True,
            name="GCScript Editor",
            icon="📜"
        )
        yield Footer()
        
        with VerticalScroll(id="project-screen"):
            yield Input()
    
    @work
    async def on_mount(self):
        pass