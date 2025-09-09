package tree_sitter_gcscript_test

import (
	"testing"

	tree_sitter "github.com/tree-sitter/go-tree-sitter"
	tree_sitter_gcscript "github.com/tree-sitter/tree-sitter-gcscript/bindings/go"
)

func TestCanLoadGrammar(t *testing.T) {
	language := tree_sitter.NewLanguage(tree_sitter_gcscript.Language())
	if language == nil {
		t.Errorf("Error loading gcscript grammar")
	}
}
