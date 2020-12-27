import socket

ip = 'localhost'
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))


s.sendall(b'Connecte')
while True : 
    message = input("Entrez un message à envoyer\n").encode("utf-8")
    s.sendall(bytes(message))
    data = s.recv(1024)
    print(repr(data), 'Reçue')
s.close()
