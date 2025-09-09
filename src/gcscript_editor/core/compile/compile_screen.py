from textual.app import ComposeResult
from textual.binding import Binding
from textual.screen import Screen
from textual.widgets import Footer, Header, RichLog, ProgressBar
from textual.containers import VerticalGroup
import asyncio as aio


class CompileScreen(Screen):
    CSS_PATH = "compile_screen.tcss"

    logger: RichLog
    done: bool = False
    BINDINGS: list[Binding] = [
        Binding("escape", "leave_compiler", "Back to editor")
    ]
        
    async def run(self):
        self.logger.write("foo")
        for _ in range(100):
            self.get_child_by_type(VerticalGroup).get_child_by_type(ProgressBar).advance(1)
            await aio.sleep(0.1)
            
    
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
        aio.create_task(self.run())

    async def action_leave_compiler(self):
        await self.app.pop_screen()