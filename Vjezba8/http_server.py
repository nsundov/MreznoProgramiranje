import SimpleHTTPServer
import SocketServer

PORT = 8000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler


httpd = SocketServer.TCPServer(("", PORT), Handler)


print "Working on port", PORT
httpd.serve_forever()