import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import receive_text
PORT = 4105

def square_for(key):
    seq=""
    for ch in (key.upper().replace("J","I")+"ABCDEFGHIKLMNOPQRSTUVWXYZ"):
        if ch.isalpha() and ch not in seq and ch!="J": seq+=ch
    return [seq[i:i+5] for i in range(0,25,5)]
key,cipher=receive_text(PORT).split("\n",1)
grid=square_for(key)
def pos(ch):
    for r,row in enumerate(grid):
        if ch in row:return r,row.index(ch)
def dec_pair(a,b):
    r1,c1=pos(a);r2,c2=pos(b)
    if r1==r2:return grid[r1][(c1-1)%5]+grid[r2][(c2-1)%5]
    if c1==c2:return grid[(r1-1)%5][c1]+grid[(r2-1)%5][c2]
    return grid[r1][c2]+grid[r2][c1]
plain="".join(dec_pair(cipher[i],cipher[i+1]) for i in range(0,len(cipher),2))
print("Decrypted (remove filler X if appropriate):",plain)

