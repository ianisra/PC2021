import socket
from cryptography.fernet import Fernet

TCP_IP = "127.0.0.1"
TCP_PORT = 5005
BUFFER_SIZE = 2048

sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TCP_IP, TCP_PORT))
sock.listen(1)
(conn, addr) = sock.accept()
print('Direccion de conexion:', addr)

while True:
    var= conn.recv(BUFFER_SIZE)
    conn.send(b'Enterado. Bye!')
    break
conn.close()

file = open('clave.key', 'rb')
lect = file.read()
file.close()
key = Fernet(lect)

dec= key.decrypt(var, None)
mensaje= dec.decode()

print(mensaje)
