import argparse
import socket
from cryptography.fernet import Fernet

TCP_IP= "127.0.0.1"
TCP_PORT= 5005
BUFFER_SIZE= 2048

description = '''Ejemplos de uso:
+ Enviar mensajes
    -msg "[contenido del mensaje]"
    *usar comillas es clave
'''

parser = argparse.ArgumentParser(description= 'Envio de mensajes', epilog= description,
                                formatter_class= argparse.RawDescriptionHelpFormatter)
parser.add_argument("-msg", metavar= "MENSAJE", dest="msg", help="Mensaje a enviar", required= True)

params = parser.parse_args()
msg = params.msg

key = Fernet.generate_key()
f = Fernet(key)

file = open('clave.key', 'wb')
file.write(key)
file.close()

enc = msg.encode()
token= f.encrypt(enc)
print("Mensaje enviado:", enc)

sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))
sock.send(token)
response= sock.recv(BUFFER_SIZE).decode()
sock.close

print(response)
