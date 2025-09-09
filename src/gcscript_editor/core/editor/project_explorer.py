from textual import on
from textual.app import ComposeResult
from textual.widgets import DirectoryTree, Static

from pathlib import Path
from typing import Iterable

class _FilteredDirectoryTree(DirectoryTree):
    def filter_paths(self, paths: Iterable[Path]) -> Iterable[Path]:
        return [path for path in paths if
                (not (path.name.startswith(".") or path.name.startswith("_")))
                and (path.is_dir() or path.suffix == ".gc")
        ]

class ProjectExplorer(Static):
    structure: _FilteredDirectoryTree = _FilteredDirectoryTree("./tests")
    
    def compose(self) -> ComposeResult:
        yield self.structure
    
    @on(structure.FileSelected)
    def pick_file(self,file:DirectoryTree.FileSelected):
        self.screen.editor.open_file(file.path) #type: ignore