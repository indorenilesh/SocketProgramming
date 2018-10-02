# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:29:36 2018

@author: nilesh_indore

This program is to send data in chunks and at client end join those chunks
"""

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',9000))
s.listen(5)
while 2>1:
    data,addr = s.accept()
    print("Connection received from ", addr)
    msg = data.recv(1024)
    data.sendall(str(msg).encode('utf-8'))
s.close()