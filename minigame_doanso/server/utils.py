def broadcast(message, clients):
    for client in clients:
        try:
            client.sendall(message.encode())
        except:
            pass
