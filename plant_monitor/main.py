#! /usr/bin/env python3

## ^^ For Unix compatability, I think it is ignored by Windows

from micropyserver import MicroPyServer

server = MicroPyServer(host="0.0.0.0", port=8000)
content =''
indexFile = 'index.html'

def index(request):
    print('<--- Received Request')
    contentLength = len(content.encode())
    response = f'HTTP/1.0 200 OK\r\nContent-Type: text/html; Content-Length: {contentLength}; Connection: close; charset=UTF-8\r\n'
    response += "\r\n"
    response += content
    server.send(response)
    print('---> Response Sent')


def stop(request):
    server.stop()

with open(indexFile, 'r') as file:
    content = file.read()

server.add_route("/", index)
server.add_route("/stop", stop)

server.start()