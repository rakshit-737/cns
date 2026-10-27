import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import receive_text
PORT = 4107

rails_text,cipher=receive_text(PORT).split("\n",1); rails=int(rails_text)
n=len(cipher); pattern=[]; row=0; direction=1
for _ in range(n):
    pattern.append(row)
    if row==0: direction=1
    elif row==rails-1: direction=-1
    row+=direction
counts=[pattern.count(r) for r in range(rails)]
chunks=[]; idx=0
for count in counts: chunks.append(cipher[idx:idx+count]); idx+=count
positions=[0]*rails; plain=""
for r in pattern:
    plain+=chunks[r][positions[r]]; positions[r]+=1
print("Decrypted message:",plain)

