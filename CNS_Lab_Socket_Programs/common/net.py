import socket

HOST = "127.0.0.1"

def send_text(port, text):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, port))
        sock.sendall(text.encode("utf-8"))
        sock.shutdown(socket.SHUT_WR)

def receive_text(port, prompt="Waiting for client..."):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, port))
        server.listen(1)
        print(prompt)
        conn, addr = server.accept()
        with conn:
            chunks = []
            while True:
                part = conn.recv(4096)
                if not part:
                    break
                chunks.append(part)
        return b"".join(chunks).decode("utf-8")
