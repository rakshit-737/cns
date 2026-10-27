# Educational localhost simulation: Alice sends her public value to Eve.
import socket
p,g,a=23,5,4
A=pow(g,a,p)
with socket.socket() as s:
    s.connect(("127.0.0.1",4111)); s.sendall(f"{p} {g} {A}".encode())
    B_fake=int(s.recv(1024).decode())
print("Alice public value:",A)
print("Alice believes Bob's public value is:",B_fake)
print("Alice's key with Eve:",pow(B_fake,a,p))
