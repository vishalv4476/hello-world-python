import http.server
import socketserver
import threading
import time
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

from urllib.parse import urlparse
from urllib.parse import parse_qs

from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)

        # Setting the header
        self.send_header("Content-type", "text/html")

        # Whenever using 'send_header', you also have to call 'end_headers'
        self.end_headers()

        # Extract query param
        name = 'World'
        self.parse_url_params(self.path)
        query_components = parse_qs(urlparse(self.path).query)

        if 'name' in query_components:
            name = query_components["name"][0]

        html = f"<html><head></head><body><h1>Hello {name}, Query Params: {query_components}!</h1></body></html>"

        # Writing the HTML contents with UTF-8
        self.wfile.write(bytes(html, "utf8"))

    def parse_url_params(self, url_path: str) -> dict:
        return parse_qs(urlparse(url_path).query)


httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()
