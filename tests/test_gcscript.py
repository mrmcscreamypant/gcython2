import gcscript
import textx

class TestPackage:
    def test_import(self):
        assert gcscript.__doc__
    
    def test_mm(self):
        print(textx.metamodel_for_file("foo.gc"))