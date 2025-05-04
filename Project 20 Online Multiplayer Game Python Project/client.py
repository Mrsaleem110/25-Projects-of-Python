import socket
import threading
import sys

HOST = input("Enter server IP (e.g., 127.0.0.1): ")
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            msg = client.recv(1024).decode()
            if not msg:
                break
            print(msg)
        except:
            break

threading.Thread(target=receive_messages, daemon=True).start()

while True:
    try:
        guess = input()
        client.sendall(guess.encode())
    except KeyboardInterrupt:
        print("\nDisconnected from the server.")
        client.close()
        sys.exit()
