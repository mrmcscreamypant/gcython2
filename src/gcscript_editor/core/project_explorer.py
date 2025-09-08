from textual.app import ComposeResult
from textual.widgets import Tree, Static, Pretty, RichLog
from textual.widgets.tree import TreeNode

import os, pathlib

class ProjectExplorer(Static):
    structure: Tree[str] = Tree("files")
    debug: RichLog = RichLog()
    
    def compose(self) -> ComposeResult:
        self._refresh_structure()
        yield self.structure
        yield self.debug
    
    def bug(self,obj) -> None:
        self.debug.write(obj,animate=True,width=25)
    
    def _dig(self,branch:os.PathLike|str,parentmatter:TreeNode) -> None:
        branchmap = os.scandir(branch)
        branchmatter = parentmatter.add(pathlib.Path(branch).name)
        self.bug(branchmap)
        for fork in branchmap:
            if fork.name[0] == ".":
                continue
            if fork.is_dir():
                self._dig(fork, branchmatter)
            if pathlib.Path(fork.path).suffix == ".gc":
                self.bug(fork)
                branchmatter.add_leaf("📜 "+pathlib.Path(fork).stem)
        
        self._prune(branchmatter)
        
    
    def _prune(self, branchmatter:TreeNode):
        if len(branchmatter.children) <= 0:
            if not branchmatter.is_root:
                pass#branchmatter.remove()
            if branchmatter.parent:
                self._prune(branchmatter.parent)
    
    def _refresh_structure(self) -> None:
        self.structure.show_root = False
        self.structure.clear()
        self._dig(".",self.structure.root)
        self.structure.root.expand()