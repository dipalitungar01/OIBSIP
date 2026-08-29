import socket
import threading


HOST = "127.0.0.1"
PORT = 5000


def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()

            if not message:
                break

            print("\n" + message)

        except:
            break


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, PORT))
except ConnectionRefusedError:
    print("Unable to connect to the server.")
    print("Please start server.py first.")
    exit()


name = input("Enter your name: ")

client.send(name.encode())

receive_thread = threading.Thread(
    target=receive_messages,
    args=(client,)
)

receive_thread.daemon = True
receive_thread.start()


print("Connected to the chat.")
print("Type your message and press Enter.")
print("Type /quit to leave.\n")


while True:
    message = input()

    if message.lower() == "/quit":
        print("You left the chat.")
        client.close()
        break

    if message.strip():
        try:
            client.send(message.encode())
        except:
            print("Connection lost.")
            break