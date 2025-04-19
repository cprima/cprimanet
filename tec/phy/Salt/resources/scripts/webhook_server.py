from http.server import BaseHTTPRequestHandler, HTTPServer

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(post_data.decode('utf-8'))
        
        self.send_response(200)
        self.end_headers()

if __name__ == "__main__":
    server_address = ('', 8001)  # Listen on all interfaces, port 8001
    httpd = HTTPServer(server_address, WebhookHandler)
    print('Webhook server started on port 8001...')
    httpd.serve_forever()

