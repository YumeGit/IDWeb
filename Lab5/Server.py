import socket
import threading

# Функция, которая будет выполняться для каждого клиента
def handle_client(client_socket, address):
    print(f"Подключение от {address}")

    # Получение и отправка данных
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        response = f"Получено сообщение: {data.decode('utf-8')}"
        client_socket.send(response.encode('utf-8'))

    # Закрытие соединения с клиентом
    print(f"Соединение с {address} закрыто")
    client_socket.close()

# Адрес и порт, на которых сервер будет прослушивать подключения
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

# Создание сокета для сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)
print(f"Сервер слушает на {SERVER_HOST}:{SERVER_PORT}")

# Принятие подключений и обработка каждого клиента в отдельном потоке
while True:
    client_socket, address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
