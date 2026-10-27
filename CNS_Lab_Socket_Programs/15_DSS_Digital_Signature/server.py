import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import receive_text
PORT = 4141

import hashlib
p,q,g=23,11,4
x=3; y=pow(g,x,p)
message,sig=receive_text(PORT).rsplit("\n",1)
r,s=map(int,sig.split())
H=int(hashlib.sha256(message.encode()).hexdigest(),16)%q
try:
    w=pow(s,-1,q)
except ValueError:
    print("Invalid signature"); raise SystemExit
u1=(H*w)%q; u2=(r*w)%q
v=(pow(g,u1,p)*pow(y,u2,p)%p)%q
print("Message:",message)
print("Signature:",(r,s))
print("Verification:", "VALID" if v==r else "INVALID")

