import http.server
import socketserver

port = 8000
host = "http://127.0.0.1"
path_dir = "./_build/html"


class SimpleHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=path_dir, **kwargs)


with socketserver.TCPServer(("", port), SimpleHandler) as httpd:
    print("server run ports:", f"{host}:{port}/")
    httpd.serve_forever()
