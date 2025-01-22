from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

# Serve the HTML content with a basic response
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve the HTML page for the user
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            with open("web/Untitled-1", "r") as file:
                self.wfile.write(bytes(file.read(), "utf-8"))

        # Serve the CSS file (if needed)
        elif self.path == "/Untitled-2":
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()

            with open("web/Untitled-2", "r") as file:
                self.wfile.write(bytes(file.read(), "utf-8"))

        # Serve JS (if you decide to add interactivity later)
        elif self.path == "/script.js":
            self.send_response(200)
            self.send_header("Content-type", "application/javascript")
            self.end_headers()

            with open("web/script.js", "r") as file:
                self.wfile.write(bytes(file.read(), "utf-8"))

        # Serve the Contact form results (POST request handling)
        elif self.path.startswith("/submit"):
            # Parse form data if it's available (For contact form or other requests)
            parsed_path = urllib.parse.urlparse(self.path)
            parsed_query = urllib.parse.parse_qs(parsed_path.query)

            name = parsed_query.get("name", ["Anonymous"])[0]
            message = parsed_query.get("message", ["No message provided"])[0]

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # Here, you can craft a response based on the form data, or render a confirmation page
            self.wfile.write(bytes(f"""
                <html>
                    <head>
                        <title>Contact Form Submitted</title>
                        <link rel="stylesheet" href="Untitled-2">
                    </head>
                    <body>
                        <div class="container">
                            <h1>Thank You, {name}!</h1>
                            <p>Your message has been received:</p>
                            <blockquote>"{message}"</blockquote>
                            <p>We will get back to you shortly!</p>
                            <a href="/">Go back to home</a>
                        </div>
                    </body>
                </html>
            """, "utf-8"))

        else:
            # If the path doesn't match any of the above, send a 404 response
            self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes("Page not found", "utf-8"))

# Setting up the server
def run(server_class=HTTPServer, handler_class=MyHandler, port=8080):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
