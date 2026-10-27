import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.net import send_text
PORT=4120

from des_core import parse_hex64, IP, permute
v=parse_hex64("Enter 64-bit input in hex: ")
out=permute(v,IP,64)
print("After Initial Permutation:",f"{out:016X}")
send_text(PORT,f"{v:016X}")
