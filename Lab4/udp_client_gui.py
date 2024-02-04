import socket
import tkinter as tk

def send_message():
    message = entry.get()
    client_socket.sendto(message.encode(), server_address)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 12345)

root = tk.Tk()
root.title("UDP Client")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)
send_button = tk.Button(root, text="Сообщение", command=send_message)
send_button.pack()

root.mainloop()
