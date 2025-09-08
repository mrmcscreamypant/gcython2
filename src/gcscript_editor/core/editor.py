from textual.app import ComposeResult
from textual.widgets import TextArea, Static

class Editor(Static):
    """
    The main text editor
    """
    
    text_area: TextArea = TextArea.code_editor()
    
    def compose(self) -> ComposeResult:
        yield self.text_area