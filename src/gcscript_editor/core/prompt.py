from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Label
from textual import on

class Prompt(Screen[bool]):
    """Screen with a parameter."""

    def __init__(self, question: str, true_text: str = "Yes", false_text: str = "No") -> None:
        self.question = question
        self.true_text = true_text
        self.false_text = false_text
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Label(self.question)
        yield Button(self.true_text, id="yes", variant="success")
        yield Button(self.false_text, id="no")

    @on(Button.Pressed, "#yes")
    def handle_yes(self) -> None:
        self.dismiss(True)  

    @on(Button.Pressed, "#no")
    def handle_no(self) -> None:
        self.dismiss(False)  