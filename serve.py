#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer
import time

class SlowHTTPHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        time.sleep(.2)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpd = SocketServer.TCPServer(("", 8000), SlowHTTPHandler)
httpd.serve_forever()
