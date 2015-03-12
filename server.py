import BaseHTTPServer
import urlparse
import time
import os

class WebRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        message_parts = [
            "<html>",
            "<head><title>Hello World</title></head>",
            "<body style=\"text-align:center;\">",
            "<p><img src='alauda.jpg' /></p>",
            "<b>Hello world! Hello Alauda!</b>",
            "</body>",
            "<html>"
        ]
        message = '\r\n'.join(message_parts)

        # message = "New request arrived from %s:%d" % self.client_address 
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message)




if __name__ == '__main__':
    print "Server started, Listening on port 80"
    server = BaseHTTPServer.HTTPServer(('0.0.0.0',80), WebRequestHandler)
    server.serve_forever()

