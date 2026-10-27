import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.net import send_text
PORT=4124

from des_core import permute, P
v=int(input("Enter 32-bit S-box output in hex: "),16)
if not 0<=v<2**32: raise SystemExit("Must be 32 bits.")
print("After P permutation:",f"{permute(v,P,32):08X}")
send_text(PORT,f"{v:08X}")
