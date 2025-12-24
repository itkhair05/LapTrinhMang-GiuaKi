# 🎮 Mini Game Đoán Số – Lập Trình Mạng (Giữa Kỳ)

## 📌 Giới thiệu

Đây là **dự án lập trình mạng Python** theo mô hình **Client – Server**, phục vụ bài **giữa kỳ môn Lập Trình Mạng**.

Ứng dụng là một **mini game đoán số**:

* Server sinh ra một số ngẫu nhiên.
* Nhiều client có thể kết nối đồng thời.
* Client gửi số dự đoán.
* Server phản hồi kết quả: **HIGH / LOW / CORRECT**.

Dự án tập trung vào:

* Lập trình socket TCP
* Xử lý đa luồng (threading)
* Giao tiếp client–server
* Thiết kế code theo module (OOP)

---

## 🧱 Kiến trúc hệ thống

```text
Client (Tkinter GUI)
   │
   │ TCP Socket
   ▼
Server (Multi-thread)
```

* **Server**: Python Socket + Threading
* **Client**: Python + Tkinter GUI
* **Giao thức**: Text-based protocol đơn giản

---

## 📁 Cấu trúc thư mục

```text
LapTrinhMang-GiuaKi-main/
│
├── anhsanpham/
│   ├── client.png          # Hình minh họa client
│   └── server.png          # Hình minh họa server
│
├── minigame_doanso/
│   ├── client/
│   │   ├── client_gui.py   # Giao diện client (Tkinter)
│   │   ├── network.py      # Xử lý kết nối socket
│   │   └── config.py       # Cấu hình client
│   │
│   ├── server/
│   │   ├── server.py       # Chương trình server chính
│   │   ├── client_handler.py # Xử lý từng client
│   │   ├── game_logic.py   # Logic đoán số
│   │   ├── utils.py        # Hàm hỗ trợ
│   │   └── config.py       # Cấu hình server
│   │
│   ├── docs/
│   │   └── protocol.txt    # Mô tả giao thức
│   │
│   └── requirements.txt    # Thư viện cần cài
```

---

## 🔌 Giao thức truyền thông

File: `docs/protocol.txt`

```text
Client gửi số đoán
Server trả về:
- HIGH     (Số đoán lớn hơn số bí mật)
- LOW      (Số đoán nhỏ hơn số bí mật)
- CORRECT  (Đoán đúng)
```

---

## ⚙️ Công nghệ sử dụng

* **Ngôn ngữ**: Python 3
* **Networking**: socket (TCP)
* **Đa luồng**: threading
* **Giao diện**: Tkinter
* **Mô hình**: Client – Server

---

## ▶️ Hướng dẫn cài đặt & chạy

### 1️⃣ Cài đặt môi trường

```bash
pip install -r requirements.txt
```

> (Tkinter thường đã có sẵn trong Python)

---

### 2️⃣ Chạy Server

```bash
cd minigame_doanso/server
python server.py
```

Server sẽ:

* Lắng nghe kết nối client
* Sinh số ngẫu nhiên
* Xử lý nhiều client cùng lúc

---

### 3️⃣ Chạy Client

```bash
cd minigame_doanso/client
python client_gui.py
```

* Nhập số vào ô input
* Nhấn **Guess** để gửi lên server
* Nhận phản hồi trực tiếp trên giao diện

---

## ✨ Chức năng chính

### Server

* Lắng nghe nhiều client cùng lúc
* Quản lý game đoán số
* Phản hồi chính xác HIGH / LOW / CORRECT
* Giới hạn số lần đoán

### Client

* Giao diện đồ họa thân thiện
* Kết nối socket đến server
* Gửi số đoán
* Hiển thị kết quả từ server

---

## 🔒 Điểm kỹ thuật nổi bật

* Sử dụng **Threading** để xử lý đa client
* Tách rõ **network – logic – UI**
* Dễ mở rộng sang:

  * Chat real-time
  * Game nhiều phòng
  * Ghi log người chơi

---

## 🚀 Hướng phát triển

* Thêm hệ thống điểm số
* Giới hạn thời gian đoán
* Chat giữa các client
* Deploy server trên VPS
* Chuyển sang WebSocket / gRPC

---

## 👨‍🎓 Thông tin môn học

* **Môn**: Lập Trình Mạng
* **Bài**: Giữa kỳ
* **Chủ đề**: Ứng dụng Client–Server chịu tải cơ bản

---

## 📜 License

Dự án phục vụ mục đích **học tập**.

---

✅ README này có thể dùng **nộp bài / GitHub / báo cáo**.
Nếu bạn muốn mình:

* Viết **báo cáo Word/PDF**
* Vẽ **sơ đồ kiến trúc**
* Đánh giá theo **rubric giảng viên**

👉 cứ nói, mình làm tiếp cho bạn.
