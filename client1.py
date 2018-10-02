# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:29:48 2018

@author: nilesh_indore
"""

import socket
s = socket.socket()
s.connect(('localhost',9000))
data = "This is test para to send to server with multiple chunk so at server end multiple chunk can be joined and read."
s.send(data.encode('utf-8'))
print(len(data))
fragments = [] # List of chunks
while True:
    chunk = s.recv(50) # Get a chunk

#Below code is to decode data first then join it
# but it's very slow
    
#    strchunk = chunk.decode('utf-8')
#    fragments.append(strchunk)
#    if len(chunk) < 50:
#        break # EOF. No more data
#print ("".join(fragments))
#s.close()

## below line of code for if you don't want
# to decode and print data directly
#just comment 17-22 and uncomment below lines

    fragments.append(chunk)
    if len(chunk) < 50:
        break # EOF. No more data
print (b"".join(fragments))
s.close()    

    

