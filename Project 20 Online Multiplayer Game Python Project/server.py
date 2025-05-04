import socket
import threading
import random

HOST = '0.0.0.0'
PORT = 5555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"[SERVER STARTED] Listening on {HOST}:{PORT}")

clients = []
secret_number = random.randint(1, 100)
winner = None

def handle_client(conn, addr):
    global winner
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.sendall(b"Welcome to the Number Guessing Game! Guess a number between 1 and 100.\n")
    
    while not winner:
        try:
            guess = conn.recv(1024).decode().strip()
            if not guess:
                break
            guess = int(guess)

            if guess == secret_number:
                winner = addr
                conn.sendall(b" You guessed it right! You win!\n")
                broadcast(f"[GAME OVER] {addr} has guessed the number {secret_number}!".encode(), conn)
            elif guess < secret_number:
                conn.sendall(b"Too low. Try again:\n")
            else:
                conn.sendall(b"Too high. Try again:\n")
        except:
            break
    
    conn.close()

def broadcast(message, winner_conn):
    for client in clients:
        if client != winner_conn:
            try:
                client.sendall(message)
            except:
                client.close()

while True:
    conn, addr = server.accept()
    clients.append(conn)
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
