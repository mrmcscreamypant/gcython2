from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

from .editor import Editor
from .project_explorer import ProjectExplorer

class GCScriptApp(App):
    """An editor for the GCScript Language"""
    
    editor: Editor = Editor()
    explorer: ProjectExplorer = ProjectExplorer()
    
    def compose(self) -> ComposeResult:
        yield Header(
            show_clock=True,
            name="GCScript Editor",
            icon="📜"
        )
        yield Footer()
        
        yield self.explorer
        
        yield self.editor
    
if __name__ == "__main__":
    app = GCScriptApp()
    app.run()