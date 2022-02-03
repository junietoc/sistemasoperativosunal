import socket
import ssl

target_host = "www.buda.com"
# puerto 443, el cual está abierto para escuchar conexiones TCP
target_port = 443
context = ssl.create_default_context()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# se envuelve el socket con SSL para solicitar datos a Buda de manera segura
client = context.wrap_socket(client, server_hostname=target_host)

client.connect((target_host, target_port))

def obtenerInfoMercadoBitcoin():
    # se obtiene la moneda de cambio y la moneda de pago en el mercado de Bitcoin
    request = "GET /api/v2/markets/btc-clp HTTP/1.1\r\nHost: %s\r\n\r\n" % target_host
    client.send(request.encode())
    f = open("market BTC.txt", "w")
    data = ""
    while data.strip() != "0":
        response = client.recv(4096)
        data = response.decode()

        f.write(data + "\n")

    f.close()

def obtenerTickerMercadoBitcoin():
    # se obtiene la información del ticker en el mercado del Bitcoin
    request = "GET /api/v2/markets/btc-clp/ticker HTTP/1.1\r\nHost: %s\r\n\r\n" % target_host
    client.send(request.encode())
    f = open("ticker BTC.txt", "w")

    data = ""
    #while data.strip() != "0":
    print(f"DATA: {data}")
    response = client.recv(4096)
    data = response.decode()
    f.write(data)

    f.close()

def obtenerLibroMercadoBitcoin():
    # se obtiene la información del libro de ordenes en el mercado del Bitcoin
    request = "GET /api/v2/markets/btc-clp/order_book HTTP/1.1\r\nHost: %s\r\n\r\n" % target_host
    client.send(request.encode())
    f = open("orderBook BTC.txt", "w")
    data = ""
    while data.strip() != "0":
        response = client.recv(4096)
        data = response.decode()
        f.write(data)

    f.close()

obtenerInfoMercadoBitcoin()
obtenerTickerMercadoBitcoin()
obtenerLibroMercadoBitcoin()