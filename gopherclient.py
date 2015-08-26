#!/usr/bin/env python
#gopherclient

import socket, sys
port = 70
host = sys.argv[1]
print "Host Name = %s" %host
filename = sys.argv[2]
print "File Name = %s" %filename

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "S = %s" %s
s.connect((host,port))

s.sendall(filename + "\r\n")


while 1:
	buf = s.recv(2048)
	if not len(buf):
		break
	sys.stdout.write(buf)