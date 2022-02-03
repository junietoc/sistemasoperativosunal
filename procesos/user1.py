#ejercicio de socket: este es un chat simple cliente servidor con capacidad de 5 mensajes.
# user1.py es el servidor y esta atento escuchando conexiones y mensajes al recibir un mensaje
# habilita la entrada de texto para mandar un mensaje a user2.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    data = clientsocket.recv(1024)
    if not data:
        break

    print(f'user2: {data.decode("utf-8")}')
    text = input("You: ")
    clientsocket.sendall(str.encode(text))
