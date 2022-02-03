from socket import *
import asyncio
# servidor web
async def webServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.setblocking(False)
    serversocket.bind(('localhost',9000))
    serversocket.listen()
    # se carga el HTML del archivo web.html
    f = open('web.html', 'r')
    webPage = f.read()
    loop = asyncio.get_event_loop()
    while(1):
        # bucle while para estar escuchando conexiones, de manera asíncrona
        (clientsocket, address) = await loop.sock_accept(serversocket)
        # información protocolo HTTP
        data = "HTTP/1.1 200 OK\r\n"
        data += "Content-Type: text/html; charset=utf-8\r\n"
        data += "\r\n"
        # se concatena el HTML
        data += webPage
        data += "\r\n\r\n"
        # se transforma en bytes la información a enviar al cliente
        clientsocket.sendall(data.encode())
        # se deja de recibir datos por parte del cliente hacia el servidor
        clientsocket.shutdown(SHUT_WR)


    serversocket.close()

asyncio.run(webServer())