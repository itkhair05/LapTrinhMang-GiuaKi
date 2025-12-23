import socket
import threading
from config import HOST, PORT, MAX_GUESS
from game_logic import GuessGame
from client_handler import handle_client

class GuessServer:
    def __init__(self):
        self.clients = []
        self.client_id = 0
        self.lock = threading.Lock()
        self.game = GuessGame()
        self.max_guess = MAX_GUESS

    def next_client_id(self):
        with self.lock:
            self.client_id += 1
            return self.client_id

    def broadcast(self, message):
        for c in self.clients:
            try:
                c.sendall(message.encode())
            except:
                pass

    def remove_client(self, conn):
        if conn in self.clients:
            self.clients.remove(conn)

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen()

        print(f"[SERVER] Listening on port {PORT}")
        print(f"[GAME] Guess number from {self.game.target}")

        while True:
            conn, addr = server.accept()
            self.clients.append(conn)
            threading.Thread(
                target=handle_client,
                args=(conn, addr, self),
                daemon=True
            ).start()

if __name__ == "__main__":
    GuessServer().start()
