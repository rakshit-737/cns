import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import send_text
PORT = 4105

import string
def square_for(key):
    seq = ""
    for ch in (key.upper().replace("J","I") + string.ascii_uppercase.replace("J","")):
        if ch.isalpha() and ch not in seq and ch != "J":
            seq += ch
    return [seq[i:i+5] for i in range(0,25,5)]
def prepare(msg):
    msg = "".join(ch for ch in msg.upper().replace("J","I") if ch.isalpha())
    out=[]; i=0
    while i < len(msg):
        a=msg[i]
        if i+1 == len(msg):
            b="X"; i+=1
        elif msg[i+1] == a:
            b="X"; i+=1
        else:
            b=msg[i+1]; i+=2
        out.append(a+b)
    return "".join(out)
key=input("Enter key: ")
msg=input("Enter message: ")
grid=square_for(key); prepared=prepare(msg)
def pos(ch):
    for r,row in enumerate(grid):
        if ch in row: return r,row.index(ch)
def enc_pair(a,b):
    r1,c1=pos(a); r2,c2=pos(b)
    if r1==r2: return grid[r1][(c1+1)%5]+grid[r2][(c2+1)%5]
    if c1==c2: return grid[(r1+1)%5][c1]+grid[(r2+1)%5][c2]
    return grid[r1][c2]+grid[r2][c1]
cipher="".join(enc_pair(prepared[i],prepared[i+1]) for i in range(0,len(prepared),2))
print("Ciphertext:",cipher)
send_text(PORT,key+"\n"+cipher)

