from textual.binding import Binding
from textual.app import App, SystemCommand
from textual.screen import Screen
from typing import Iterable

from gcscript_editor.core.editor.editor_screen import EditorScreen
from gcscript_editor.core.compile.compile_screen import CompileScreen


class GCScriptApp(App):
    """An editor for the GCScript Language"""
    CSS_PATH = "project_explorer.tcss"
    
    BINDINGS = [
        Binding("ctrl+w","close_tab"),
    ]
    
    SCREENS = {
        "editor": EditorScreen,
        "compiler": CompileScreen
    }
    
    def on_mount(self) -> None:
        self.push_screen("compiler")
        
    def get_system_commands(self, screen: Screen) -> Iterable[SystemCommand]:
        yield from super().get_system_commands(screen)
        self.log(screen.name)
        if type(screen) == EditorScreen:
            yield SystemCommand("Compile", "Compile the program", screen.action_switch_to_compile)

if __name__ == "__main__":
    app = GCScriptApp()
    app.run()