#ejercicio de socket: este es un chat simple cliente servidor con capacidad de 5 mensajes.
# user2.py es el cliente y para mandar mensajes se conecta al servidor user1.py, recibe entrada de texto
# y envia la informacion
import socket

for i in range(5):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))
    text = input("You: ")
    s.sendall(str.encode(text))
    msg = s.recv(1024)
    print(f'user1: {msg.decode("utf-8")}')