/**
 * @file A languguge that compiles to Desmos
 * @author john <nil>
 * @license MIT
 */

/// <reference types="tree-sitter-cli/dsl" />
// @ts-check

module.exports = grammar({
  name: "gcscript",

  rules: {
    // TODO: add the actual grammar rules
    source_file: $ => "hello"
  }
});
