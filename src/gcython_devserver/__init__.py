from bottle import Bottle, response
from pathlib import Path
from os.path import dirname
import json

from gcython.VM import CompiledVM

class GCDevserver(Bottle):
    vm: CompiledVM;

    def __init__(self, vm: CompiledVM):
        super().__init__()

        self.vm = vm

        self.route("/")(self.index) #type: ignore
        self.route("/index.js")(self.js) #type: ignore
        self.route("/index.css")(self.css) #type: ignore
        self.route("/latex")(lambda: self.latex(self)) #type: ignore
    
    @staticmethod
    def index():
        with open(Path(dirname(__file__),"./index.html")) as file:
            html = file.read()
        return html

    @staticmethod
    def js():
        response.content_type = "text/javascript"
        with open(Path(dirname(__file__),"./index.js")) as file:
            js = file.read()
        return js

    @staticmethod
    def css():
        response.content_type = "text/css"
        with open(Path(dirname(__file__),"./index.css")) as file:
            css = file.read()
        return css

    @staticmethod
    def latex(this):
        response.content_type = "text/json"
        return json.dumps(this.vm.expressions)