from http.server import HTTPServer, BaseHTTPRequestHandler

NAME = "Esha Fatima"
PORT = 8080


class Greeter(BaseHTTPRequestHandler):
    def do_GET(self):
        html = (
            f"<h1>Hey, {NAME}!</h1>"
            "<p>Quote of the day: Ship it, then polish it.</p>"
        )
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())


if __name__ == "__main__":
    print(f"Greeter running on port {PORT}", flush=True)
    HTTPServer(("0.0.0.0", PORT), Greeter).serve_forever()