import socket
import threading

class ClientNetwork:
    def __init__(self, host, port, on_message):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.on_message = on_message

        threading.Thread(target=self.listen, daemon=True).start()

    def listen(self):
        while True:
            try:
                data = self.sock.recv(1024).decode()
                if data:
                    self.on_message(data)
            except:
                break

    def send_guess(self, number):
        self.sock.sendall(f"GUESS:{number}".encode())
