import socket

ip = 'localhost'
port = 9999
timeout = 5 #nombre de secondes d'attente de connexion après lancement du script jcrois  


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ouverture du socket
s.bind((ip, port)) 
s.listen(timeout)#attente de connexion
conn, addr = s.accept() #on accepte la connexion

while True:
    data = conn.recv(1024) # on recoit des paquets de 1024 bits en boucle et on affiche 
    print(data)
conn.close()