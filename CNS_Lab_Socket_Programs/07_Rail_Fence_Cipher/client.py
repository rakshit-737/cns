import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import send_text
PORT = 4107

msg="".join(ch for ch in input("Enter message: ").upper() if ch.isalpha())
rails=int(input("Enter number of rails (2 or more): "))
if rails<2: raise SystemExit("Rails must be at least 2.")
rows=["" for _ in range(rails)]; row=0; direction=1
for ch in msg:
    rows[row]+=ch
    if row==0: direction=1
    elif row==rails-1: direction=-1
    row+=direction
cipher="".join(rows)
print("Ciphertext:",cipher)
send_text(PORT,str(rails)+"\n"+cipher)

