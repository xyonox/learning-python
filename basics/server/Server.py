import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if(self.path) == "hi":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"hello")
        else:
            super().do_GET()

def run():
    with socketserver.TCPServer(("", 1126), MyHandler) as h:
        h.serve_forever()