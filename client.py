# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 12:01:55 2018

@author: nilesh_indore
"""

import socket
s = socket.socket()
s.connect(('localhost',9000))
data = s.recv(1024)
print(data.decode('utf-8'))
print(len(data))
s.close()

