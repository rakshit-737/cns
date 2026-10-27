import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import receive_text
PORT = 4106

vals_text,cipher=receive_text(PORT).split("\n",1)
a,b,c,d=map(int,vals_text.split())
det=(a*d-b*c)%26
inv=next((i for i in range(26) if det*i%26==1),None)
if inv is None: raise SystemExit("Invalid Hill key.")
ia,ib,ic,id=(inv*d%26,inv*(-b)%26,inv*(-c)%26,inv*a%26)
plain=""
for i in range(0,len(cipher),2):
    x,y=ord(cipher[i])-65,ord(cipher[i+1])-65
    plain+=chr((ia*x+ib*y)%26+65)+chr((ic*x+id*y)%26+65)
print("Decrypted (trailing X may be padding):",plain)

