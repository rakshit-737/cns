import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import send_text
PORT = 4106

def inv2(a,b,c,d):
    det=(a*d-b*c)%26
    inv=next((i for i in range(26) if det*i%26==1),None)
    if inv is None: raise SystemExit("Key matrix is not invertible mod 26.")
    return (inv*d%26, inv*(-b)%26, inv*(-c)%26, inv*a%26)
vals=list(map(int,input("Enter 2x2 key as a b c d: ").split()))
if len(vals)!=4: raise SystemExit("Enter four integers.")
a,b,c,d=vals
inv2(a,b,c,d)
msg="".join(ch for ch in input("Enter message: ").upper() if ch.isalpha())
if len(msg)%2: msg+="X"
out=""
for i in range(0,len(msg),2):
    x,y=ord(msg[i])-65,ord(msg[i+1])-65
    out+=chr((a*x+b*y)%26+65)+chr((c*x+d*y)%26+65)
print("Ciphertext:",out)
send_text(PORT," ".join(map(str,vals))+"\n"+out)

