# Educational localhost MITM demonstration. Run Eve first, then Bob, then Alice.
import socket, threading, time
p,g=23,5
eve_a,eve_b=7,9
A_eve=pow(g,eve_a,p); B_eve=pow(g,eve_b,p)
with socket.socket() as server:
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(("127.0.0.1",4111)); server.listen(1)
    print("Eve waiting for Alice...")
    alice,_=server.accept()
    with alice:
        p_text,g_text,A_text=alice.recv(1024).decode().split()
        p=int(p_text); g=int(g_text); A=int(A_text)
        # Forward Eve's own public value to Alice.
        alice.sendall(str(B_eve).encode())
with socket.socket() as bob:
    bob.connect(("127.0.0.1",4112))
    bob.sendall(f"{p} {g} {A_eve}".encode())
    B=int(bob.recv(1024).decode())
print("Eve key with Alice:",pow(A,eve_b,p))
print("Eve key with Bob:",pow(B,eve_a,p))
print("Eve substituted public values in this toy simulation.")
