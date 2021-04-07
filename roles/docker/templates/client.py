#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time

while True:
    sock = socket.socket()
    sock.connect(('192.168.0.2', 9090))
    sock.send('PING')
    data = sock.recv(1024)
    sock.close()
    print data
    time.sleep(5)
