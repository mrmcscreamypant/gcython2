from bottle import Bottle, response
from pathlib import Path
from os.path import dirname

class GCDevserver(Bottle):
    def __init__(self):
        super().__init__()

        self.route("/")(self.index) #type: ignore
        self.route("/index.js")(self.js) #type: ignore
        self.route("/index.css")(self.css) #type: ignore
    
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