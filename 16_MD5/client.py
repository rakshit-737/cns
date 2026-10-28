import socket
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from md5_core import md5
from common.net import send_text, receive_text

HOST, PORT = "127.0.0.1", 4142
message = input("Enter message: ")
local_digest = md5(message.encode("utf-8"))
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    send_text(client, message)
    remote_digest = receive_text(client)
print("Client MD5 :", local_digest)
print("Server MD5 :", remote_digest)
print("Match:", local_digest == remote_digest)
