import socket
import tkinter as tk

def send_message():
    message = entry_message.get()
    if message:
        try:
            client_socket.send(message.encode('utf-8'))
            response = client_socket.recv(1024)
            print("Ответ от сервера:", response.decode('utf-8'))
        except Exception as e:
            print("Ошибка при отправке сообщения:", e)
    else:
        print("Введите сообщение для отправки")

# Создаем окно приложения
root = tk.Tk()
root.title("Клиент TCP")

# Создаем виджеты
label_message = tk.Label(root, text="Сообщение:")
label_message.grid(row=0, column=0, padx=5, pady=5)

entry_message = tk.Entry(root, width=40)
entry_message.grid(row=0, column=1, padx=5, pady=5)

button_send = tk.Button(root, text="Отправить", command=send_message)
button_send.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Адрес и порт сервера
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

# Создаем сокет для клиента и подключаемся к серверу
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((SERVER_HOST, SERVER_PORT))
except Exception as e:
    print("Не удалось подключиться к серверу:", e)
    root.destroy()
else:
    # Запускаем цикл обработки событий
    root.mainloop()

# Закрываем сокет при выходе из программы
client_socket.close()