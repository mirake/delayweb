import BaseHTTPServer
import urlparse
import time
import os

class WebRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        """
        """
        parsed_path = urlparse.urlparse(self.path)
        message_parts = [
                'CLIENT VALUES:',
                'client_address=%s (%s)' % (self.client_address,
                                            self.address_string()),
                'command=%s' % self.command,
                'path=%s' % self.path,
                'real path=%s' % parsed_path.path,
                'query=%s' % parsed_path.query,
                'request_version=%s' % self.request_version,
                '',
                'SERVER VALUES:',
                'server_version=%s' % self.server_version,
                'sys_version=%s' % self.sys_version,
                'protocol_version=%s' % self.protocol_version,
                '',
                'HEADERS RECEIVED:',
                ]
        for name, value in sorted(self.headers.items()):
            message_parts.append('%s=%s' % (name, value.rstrip()))
        message_parts.append('')
        message = '\r\n'.join(message_parts)

        (ip:port) = self.client_address
        message = "from %s:%d \r\n\r\n" % (ip, port)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message)




if __name__ == '__main__':
    delays = int(os.getenv("DELAY", "10"))
    time.sleep(delays)
    print "Starting server..."
    server = BaseHTTPServer.HTTPServer(('0.0.0.0',80), WebRequestHandler)
    server.serve_forever()

