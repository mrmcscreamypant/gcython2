from gcscript_editor.core.editor.editor import Editor
from gcscript_editor.core.editor.project_explorer import ProjectExplorer


from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal
from textual.screen import Screen
from textual.widgets import Footer, Header

from gcscript_editor.core.compile.compile_screen import CompileScreen


class EditorScreen(Screen):
    editor: Editor = Editor()
    explorer: ProjectExplorer = ProjectExplorer(id="project-explorer")

    BINDINGS = [
        Binding("ctrl+r","switch_to_compile","Compile & run")
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

    async def action_switch_to_compile(self):
        await self.app.push_screen(CompileScreen())