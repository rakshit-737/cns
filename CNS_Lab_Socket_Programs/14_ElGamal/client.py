import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import send_text
PORT = 4140

import secrets
p=23; alpha=5; x=6; y=pow(alpha,x,p)
m=int(input("Enter numeric message 1-22: "))
if not 0<m<p: raise SystemExit("Message must be between 1 and p-1.")
k=secrets.randbelow(p-2)+1
C1=pow(alpha,k,p); C2=(m*pow(y,k,p))%p
print("Public key:",(p,alpha,y),"Ciphertext:",(C1,C2))
send_text(PORT,f"{C1} {C2}")

