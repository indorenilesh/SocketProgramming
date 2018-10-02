# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 11:51:44 2018

@author: nilesh_indore
"""

import socket
s = socket.socket()
s.bind(('',9000))
s.listen(5)
while 2>1:
    data,addr = s.accept()
    print("Connection received from ", addr)
    msg = 'Hello' , addr[0]
    data.send(str(msg).encode('utf-8'))
s.close()