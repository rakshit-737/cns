import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import receive_text
PORT = 4110

p_text=receive_text(PORT)
p,g,a,A=map(int,p_text.split())
b=int(input("Enter Bob's private number b: "))
B=pow(g,b,p); shared=pow(A,b,p)
print("Bob public value:",B)
print("Bob shared secret:",shared)
print("Alice shared secret (demonstration):",pow(B,a,p))

