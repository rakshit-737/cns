import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import send_text
PORT = 4109

p=int(input("Enter small prime p: ")); q=int(input("Enter small prime q: "))
n=p*q; phi=(p-1)*(q-1)
e=next((v for v in range(2,phi) if __import__("math").gcd(v,phi)==1),None)
if e is None: raise SystemExit("Choose different primes.")
d=next(v for v in range(2,phi) if (e*v)%phi==1)
m=int(input(f"Enter numeric message 0 to {n-1}: "))
if not 0<=m<n: raise SystemExit("Message must be smaller than n.")
c=pow(m,e,n)
print("Public key:",(n,e),"Private key:",(n,d),"Ciphertext:",c)
send_text(PORT,f"{n} {d}\n{c}")

