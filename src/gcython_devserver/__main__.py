from . import GCDevserver
from gcython.__main__ import App

app = GCDevserver(App().compose())
app.run(host="0.0.0.0", server="cheroot")