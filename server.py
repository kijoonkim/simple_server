from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            fn=self.path[1:]
            print(fn)
            self.send_response(200)
            self.end_headers()
            fh=open(fn,'rb')
            string=fh.read()
            self.wfile.write(string)
        except:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('404 - Not Found')

httpd = HTTPServer(('', 80), SimpleHTTPRequestHandler)
httpd.serve_forever()