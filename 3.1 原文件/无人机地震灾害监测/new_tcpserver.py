import socket, cv2, time
global conn,addr, ser_socket
def reconnect():
	host = '192.168.1.116'
	port = 23000
	ser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ser_socket.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,921600)
	ser_socket.bind((host, port))
	ser_socket.listen(1)
	conn,addr = ser_socket.accept()
	return conn,addr, ser_socket


cam = cv2.VideoCapture(0)
time.sleep(5)
def GetPhoto():
	ret, camshot = cam.read()
	camshot = cv2.resize(camshot, (640, 480), interpolation=cv2.INTER_CUBIC)
	return camshot
		
conn ,addr, ser_socket = reconnect()
print 'connecting:' + str(addr)

while(1):
	try:
		flag = conn.recv(1024)
	except:
		print 'test'
	if flag == 'start':
		new_photo = GetPhoto()
		#new_string = '1234567890'*92160
		new_string =new_photo.tostring()
		conn.sendall(new_string)
	elif flag == 'notok':
		ser_socket.close()
		conn,addr, ser_socket = reconnect()
		print 'reconnect' 

