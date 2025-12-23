import tkinter as tk
from network import ClientNetwork
from config import SERVER_HOST, SERVER_PORT

class GuessClientGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🎮 Guess The Number")

        self.log = tk.Text(self.root, height=15, width=50)
        self.log.pack(padx=10, pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.pack(padx=10)

        self.btn = tk.Button(self.root, text="Guess", command=self.send_guess)
        self.btn.pack(pady=5)

        self.network = ClientNetwork(
            SERVER_HOST,
            SERVER_PORT,
            self.on_message
        )

        self.root.mainloop()

    def on_message(self, message):
        self.log.insert(tk.END, message)
        self.log.see(tk.END)

        if message.startswith("WINNER"):
            self.entry.config(state="disabled")
            self.btn.config(state="disabled")

    def send_guess(self):
        number = self.entry.get()
        if number.isdigit():
            self.network.send_guess(number)
            self.entry.delete(0, tk.END)

if __name__ == "__main__":
    GuessClientGUI()
