from textual.app import ComposeResult
from textual.binding import Binding
from textual.screen import Screen
from textual import work
from textual.widgets import Footer, Header, RichLog, ProgressBar
from textual.containers import VerticalGroup
from gcython_devserver import GCDevserver
from gcscript import gcscript_latex_generator
from gcython.VM import VM

class Devserver(GCDevserver):
    pass

class CompileScreen(Screen):
    CSS_PATH = "compile_screen.tcss"

    logger: RichLog
    done: bool = False
    BINDINGS: list[Binding] = [
        Binding("escape", "leave_compiler", "Back to editor")
    ]
        
    @work
    async def run(self):
        Devserver(App().compose()).run(
            host="0.0.0.0",
            server="cheroot"
        )

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.logger = RichLog()

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
                yield ProgressBar(total=100)
    
    def on_mount(self) -> None:
        self.run()

    async def action_leave_compiler(self):
        await self.app.pop_screen()