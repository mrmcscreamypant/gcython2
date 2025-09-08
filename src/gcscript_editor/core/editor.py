from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import TextArea

class Editor(Widget):
    """
    The main text editor
    """
    
    text_area: TextArea = TextArea.code_editor()
    
    def compose(self) -> ComposeResult:
        yield self.text_area