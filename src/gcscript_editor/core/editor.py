from textual.app import ComposeResult
from textual.widgets import TextArea, Static, TabbedContent, TabPane, Markdown
from textual.containers import HorizontalGroup

from types import FunctionType
from pathlib import Path
from dataclasses import dataclass

@dataclass
class _OpenFile:
    
    path: Path
    _pane: TabPane|None = None
    editor: TextArea|None = None
    
    def __init__(self,path: Path):
        self.path = path
    
    def __eq__(self, value) -> bool:
        if value.__class__ != self.__class__:
            raise TypeError(f"Cannot compare {self.__class__} and {value.__class__}")
        return value.path == self.path

    def _bogus_compose(self) -> FunctionType:
        def func() -> ComposeResult:
            if self.editor:
                yield self.editor
        return func

    @property
    def tab_id(self) -> str:
        return f"d{hash(self.path)}"

    def compose(self) -> TabPane:
        if not self.editor or not self._pane:
            self.editor = TextArea.code_editor()
            self._pane = TabPane(self.path.name, id=self.tab_id)
            self._pane.compose = self._bogus_compose()
        return self._pane

class Editor(Static):
    """
    The main text editor
    """
    
    open_files: list[_OpenFile] = []
    
    def compose(self) -> ComposeResult:
        with TabbedContent():
            for file in self.open_files:
                yield file.compose()

    @staticmethod
    def create_editor(path: Path) -> TextArea:
        file = open(path.absolute())
        text = file.read()
        file.close()
        return TextArea.code_editor(text)

    def open_file(self, file: Path) -> None:
        open_file: _OpenFile = _OpenFile(file)
        if open_file in self.open_files:
            self.get_child_by_type(TabbedContent).active = open_file.tab_id
            return
        self.open_files.append(open_file)
        self.refresh(recompose=True)