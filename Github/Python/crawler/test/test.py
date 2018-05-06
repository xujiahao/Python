import argparse
from selectors import DefaultSelector, EVENT_WRITE
from socket import socket

# 网络连接的例子（socket和selectors结合）

def connected():
    selector.unregister(sock.fileno())
    print('connected!')

url = "http://www.baicu.com"
sock = socket()
sock.setblocking(False)
sock.connect(('xkcd.com', 80))
selector = DefaultSelector()
selector.register(sock.fileno(), connected())
