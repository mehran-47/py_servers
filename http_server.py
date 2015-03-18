#!/usr/bin/python3
import http.server
htmlpage = '<html><head><title>Web Page</title></head><body>Hello Python World</body></html>'
notfound = "File not found"
class WelcomeHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()
            self.wfile.write(bytes(htmlpage, 'UTF-8'))
        else:
            self.send_error(404, notfound)
httpserver = http.server.HTTPServer(("",8080), WelcomeHandler)
httpserver.serve_forever()