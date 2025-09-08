from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import DirectoryTree

class ProjectExplorer(Widget):
    def compose(self) -> ComposeResult:
        yield DirectoryTree(".")