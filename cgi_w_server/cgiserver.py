#!/usr/bin/env python3
from http.server import HTTPServer, CGIHTTPRequestHandler
from os import path, getpid

class customCGIHTTPReqHandler(CGIHTTPRequestHandler):
    """docstring for customCGIHTTPReqHandler"""
    error_message_format = '<h1>heuheuheu<h1>'
    def do_GET(self):
        if self.path=="/": self.path = '/cgi_bin/hello.py'
        super().do_GET()

if __name__ == '__main__':
    handler = customCGIHTTPReqHandler
    handler.cgi_directories = ['/cgi_bin','/htbin']
    server = HTTPServer(('192.168.252.1',8080), handler)
    print('server PID: '+ str(getpid()))
    server.serve_forever()