import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.net import send_text
PORT=4123

from des_core import parse_hex64, S, permute, E, subkeys, f
v=int(input("Enter 48-bit value in hex (after XOR with round key): "),16)
if not 0<=v<2**48: raise SystemExit("Must be 48 bits.")
out=0
for i in range(8):
    six=(v>>(42-6*i))&63
    row=((six&32)>>4)|(six&1); col=(six>>1)&15
    out=(out<<4)|S[i][row][col]
print("After 8 S-boxes (32-bit):",f"{out:08X}")
send_text(PORT,f"{v:012X}")
