#! /usr/bin/env python3

## ^^ For Unix compatability, I think it is ignored by Windows

from micropyserver import MicroPyServer
import utils

server = MicroPyServer(host="0.0.0.0", port=8000)
content =''
indexFile = 'index.html'

def index(request):
    contentLength = f"Content-Length: {str(len(content.encode()))}"
    headers = [contentLength, "Connection: close"]
    utils.send_response(server, content, extend_headers=headers)

def stop(request):
    server.stop()

with open(indexFile, 'r') as file:
    content = file.read()

server.add_route("/", index)
server.add_route("/stop", stop)

server.start()