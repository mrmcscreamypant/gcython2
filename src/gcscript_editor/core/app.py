from textual.binding import Binding
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from textual.containers import Horizontal

from .editor import Editor
from .project_explorer import ProjectExplorer

class GCScriptApp(App):
    """An editor for the GCScript Language"""
    CSS_PATH = "project_explorer.tcss"
    
    editor: Editor = Editor()
    explorer: ProjectExplorer = ProjectExplorer(id="project-explorer")
    
    BINDINGS = [
        Binding("ctrl+w","close_tab")
    ]
    
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
    
if __name__ == "__main__":
    app = GCScriptApp()
    app.run()