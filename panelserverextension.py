from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the app.ipynb directory with bokeh server"""
    Popen(["panel", "serve", "/home/jovyan/app.ipynb", "--allow-websocket-origin=*", "--port=5006"])
