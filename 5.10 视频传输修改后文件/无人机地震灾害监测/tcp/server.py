# -*- coding: UTF-8 -*-

import socket

host = '172.31.105.154'
port = 23000


ser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ser_socket.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,921600)
ser_socket.bind((host, port))
ser_socket.listen(1)
conn,addr = ser_socket.accept()
print 'connected:' + str(addr)
 

while(1):
	try:
		flag = conn.recv(1024)
	except:
		print 'test'
	if flag == 'start':
		new_string = '1234567890'*92160
		conn.sendall(new_string)
		#conn,addr = ser_socket.accept()

