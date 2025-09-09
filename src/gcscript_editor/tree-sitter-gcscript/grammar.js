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
        source_file: $ => repeat($._base_args),

        _base_args: $ => choice(
            $.import
        ),

        import: $ => seq(
            'import',
            /\*./
        ),
    }
});
