import socket
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sha512_core import sha512
from common.net import send_text, receive_text

HOST, PORT = "127.0.0.1", 4143
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"SHA-512 server listening on {HOST}:{PORT}")
    conn, addr = server.accept()
    with conn:
        print("Connected:", addr)
        message = receive_text(conn)
        digest = sha512(message.encode("utf-8"))
        print("Received:", message)
        print("SHA-512 digest:", digest)
        send_text(conn, digest)
