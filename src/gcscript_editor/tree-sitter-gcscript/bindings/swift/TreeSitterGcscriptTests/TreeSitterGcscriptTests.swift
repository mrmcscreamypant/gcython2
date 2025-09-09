import XCTest
import SwiftTreeSitter
import TreeSitterGcscript

final class TreeSitterGcscriptTests: XCTestCase {
    func testCanLoadGrammar() throws {
        let parser = Parser()
        let language = Language(language: tree_sitter_gcscript())
        XCTAssertNoThrow(try parser.setLanguage(language),
                         "Error loading gcscript grammar")
    }
}
