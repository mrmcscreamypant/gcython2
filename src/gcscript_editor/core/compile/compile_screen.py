from textual.app import ComposeResult
from textual.binding import Binding
from textual.screen import Screen
from textual.widgets import Footer, Header, RichLog, ProgressBar, Markdown
from textual.containers import VerticalGroup, Middle


class CompileScreen(Screen):
    CSS_PATH = "compile_screen.tcss"

    logger: RichLog
    done: bool = False
    BINDINGS: list[Binding] = [
        Binding("escape", "leave_compiler", "Back to editor")
    ]
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.logger = RichLog()
        self.run()
        
    def run(self):
        self.logger.write("foo")

    def compose(self) -> ComposeResult:
        yield Header(
            show_clock=True,
            name="GCScript Compiler",
            icon="📜"
        )
        yield Footer()
        
        with VerticalGroup():
            yield self.logger
            if not self.done:
                yield ProgressBar()

    async def action_leave_compiler(self):
        await self.app.pop_screen()