import socket

HOST = 'localhost'
PORT = 6379
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'PING')
    data = s.recv(1024)
print('Received', repr(data))
