# Educational localhost simulation: Bob receives Eve's forwarded public value.
import socket
p,g,b=23,5,6
B=pow(g,b,p)
with socket.socket() as server:
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(("127.0.0.1",4112)); server.listen(1)
    print("Bob waiting for Eve...")
    c,_=server.accept()
    with c:
        data=c.recv(1024).decode()
        p_text,g_text,A_text=data.split()
        A=int(A_text)
        c.sendall(str(B).encode())
print("Bob public value:",B)
print("Bob shared key with Eve:",pow(A,b,int(p_text)))
