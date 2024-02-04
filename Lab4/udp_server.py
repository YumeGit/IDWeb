import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 12345)
server_socket.bind(server_address)

print('UDP запущен.')

while True:
    data, client_address = server_socket.recvfrom(1024)

    print(f"Сообщение принято от {client_address}: {data.decode()}")

    response = "Успех !"
    server_socket.sendto(response.encode(), client_address)
