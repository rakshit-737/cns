import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.net import send_text
PORT=4122

from des_core import parse_hex64, permute, E
v=int(input("Enter 32-bit R half in hex: "),16)
if not 0<=v<2**32: raise SystemExit("Must be 32 bits.")
out=permute(v,E,32)
print("Expanded 48-bit value:",f"{out:012X}")
send_text(PORT,f"{v:08X}")
