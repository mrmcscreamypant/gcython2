from textual.binding import Binding
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer
from textual.containers import Horizontal

from .editor import Editor
from .project_explorer import ProjectExplorer

class EditorScreen(Screen):
    editor: Editor = Editor()
    explorer: ProjectExplorer = ProjectExplorer(id="project-explorer")
    
    def compose(self) -> ComposeResult:
        yield Header(
            show_clock=True,
            name="GCScript Editor",
            icon="📜"
        )
        yield Footer()
        
        with Horizontal():
            yield self.explorer
            yield self.editor

class CompileScreen(Screen):
    def compose(self) -> ComposeResult:
        
        yield Header(
            show_clock=True,
            name="GCScript Compiler",
            icon="📜"
        )
        yield Footer()

class GCScriptApp(App):
    """An editor for the GCScript Language"""
    CSS_PATH = "project_explorer.tcss"
    
    BINDINGS = [
        Binding("ctrl+w","close_tab"),
        Binding("ctrl+r","switch_to_compile","Switch to the compiler")
    ]
    
    SCREENS = {
        "editor": EditorScreen,
        "compiler": CompileScreen
    }
    
    def on_mount(self) -> None:
        self.push_screen("editor")

if __name__ == "__main__":
    app = GCScriptApp()
    app.run()