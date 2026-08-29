import socket
import threading
from datetime import datetime


HOST = "127.0.0.1"
PORT = 5000

clients = []


def get_time():
    return datetime.now().strftime("%H:%M")


def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode())
            except:
                pass


def handle_client(client, address):
    print(f"Client connected: {address}")

    try:
        name = client.recv(1024).decode()

        welcome_message = (
            f"[{get_time()}] {name} joined the chat."
        )

        print(welcome_message)
        broadcast(welcome_message, client)

        while True:
            message = client.recv(1024).decode()

            if not message:
                break

            full_message = f"[{get_time()}] {name}: {message}"

            print(full_message)
            broadcast(full_message, client)

    except ConnectionResetError:
        pass

    finally:
        if client in clients:
            clients.remove(client)

        disconnect_message = (
            f"[{get_time()}] {name} left the chat."
        )

        print(disconnect_message)
        broadcast(disconnect_message, client)

        client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()

print(f"Chat server started on {HOST}:{PORT}")
print("Waiting for clients...")

while True:
    client, address = server.accept()

    clients.append(client)

    thread = threading.Thread(
        target=handle_client,
        args=(client, address)
    )

    thread.start()