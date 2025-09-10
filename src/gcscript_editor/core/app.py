from textual import work
from textual.binding import Binding
from textual.app import App, SystemCommand
from textual.screen import Screen
from typing import Iterable
import asyncio as aio

from gcscript_editor.core.editor.editor_screen import EditorScreen
from gcscript_editor.core.project.project_screen import ProjectScreen
from gcscript_editor.core.data_storage.global_settings import GlobalSettings


class GCScriptApp(App):
    """An editor for the GCScript Language"""
    CSS_PATH = "project_explorer.tcss"
    
    BINDINGS = [
        Binding("ctrl+w","close_tab"),
    ]
    
    SCREENS = {
        "editor": EditorScreen,
        "project": ProjectScreen
    }
    
    GLOBAL_SETTINGS: GlobalSettings
    
    def on_mount(self) -> None:
        self.GLOBAL_SETTINGS = GlobalSettings.load()
        self.theme = self.GLOBAL_SETTINGS.theme
        self.push_screen("editor")
        
    def get_system_commands(self, screen: Screen) -> Iterable[SystemCommand]:
        yield from super().get_system_commands(screen)
        if type(screen) == EditorScreen:
            yield SystemCommand("Compile", "Compile the program", screen.action_switch_to_compile)

if __name__ == "__main__":
    app = GCScriptApp()
    app.run()