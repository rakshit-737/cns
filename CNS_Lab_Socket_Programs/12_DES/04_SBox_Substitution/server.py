import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.net import receive_text
PORT=4123

from des_core import S
v=int(receive_text(PORT),16); out=0
for i in range(8):
    six=(v>>(42-6*i))&63; row=((six&32)>>4)|(six&1); col=(six>>1)&15
    out=(out<<4)|S[i][row][col]
print("After 8 S-boxes (32-bit):",f"{out:08X}")
