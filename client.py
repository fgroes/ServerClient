import socket


HOST = ''
PORT = 50011
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('hello my name is frank')
data = s.recv(2048)
print('Received: {0}'.format(data))
s.sendall('i am very old')
data = s.recv(2048)
print('Received: {0}'.format(data))
s.sendall('but very horny')
data = s.recv(2048)
print('Received: {0}'.format(data))
s.sendall('disconnect')
s.close()
