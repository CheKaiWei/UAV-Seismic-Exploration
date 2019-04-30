import socket
host = '172.31.105.159'
port = 23000
address = (host, port)  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

s.connect((host, port))  
  
data = s.recv(1024)  
print 'the data received is',data  
  
s.send('hihi')  
  
s.close() 
