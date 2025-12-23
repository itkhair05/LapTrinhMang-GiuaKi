import time

def handle_client(conn, addr, server):
    client_id = server.next_client_id()
    guess_count = 0

    print(f"[KẾT NỐI] Client {client_id} đã kết nối từ {addr}")
    conn.sendall(f"THÔNG BÁO:Chào mừng Client {client_id}\n".encode())

    try:
        while True:
            data = conn.recv(1024).decode().strip()
            if not data:
                break

            if not server.game.active:
                conn.sendall("THÔNG BÁO:Trò chơi đã kết thúc. Đang chờ reset...\n".encode())
                continue

            if data.startswith("GUESS:"):
                if guess_count >= server.max_guess:
                    conn.sendall("THÔNG BÁO:Bạn đã hết lượt đoán\n".encode())
                    continue

                guess_count += 1
                number = int(data.split(":")[1])

                result = server.game.check_guess(number)

                if result == "LOW":
                    server.broadcast(
                        f"THÔNG BÁO:Client {client_id} đoán {number} → Số cần tìm LỚN HƠN\n"
                    )

                elif result == "HIGH":
                    server.broadcast(
                        f"THÔNG BÁO:Client {client_id} đoán {number} → Số cần tìm NHỎ HƠN\n"
                    )

                else:
                    # CLIENT THẮNG
                    server.game.active = False
                    server.broadcast(
                        f"CHIẾN THẮNG:🎉 Client {client_id} đã đoán ĐÚNG số ({number}) 🎉\n"
                    )

                    server.broadcast(
                        "HỆ THỐNG:Trò chơi sẽ bắt đầu lại sau 5 giây...\n"
                    )

                    time.sleep(5)

                    # RESET GAME
                    server.game.reset_game()
                    server.broadcast(
                        "HỆ THỐNG:🎮 Trò chơi mới đã bắt đầu! Hãy tiếp tục đoán.\n"
                    )

                    # Reset lượt đoán cho client thắng
                    guess_count = 0

    except:
        pass
    finally:
        print(f"[NGẮT KẾT NỐI] Client {client_id} đã ngắt kết nối")
        server.remove_client(conn)
        conn.close()
