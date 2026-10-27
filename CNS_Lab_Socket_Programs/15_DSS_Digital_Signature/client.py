import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import send_text
PORT = 4141

# Toy DSA demonstration only; never use these tiny parameters for security.
import hashlib
p,q,g=23,11,4
x=3; y=pow(g,x,p)
message=input("Enter message to sign: ")
H=int(hashlib.sha256(message.encode()).hexdigest(),16)%q
k=next(v for v in range(2,q) if __import__("math").gcd(v,q)==1)
r=pow(g,k,p)%q
s=(pow(k,-1,q)*(H+x*r))%q
if r==0 or s==0: raise SystemExit("Toy parameters produced invalid signature; run again with another message.")
print("Signature (r,s):",(r,s))
send_text(PORT,f"{message}\n{r} {s}")

