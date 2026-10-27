import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.net import send_text
PORT=4121

from des_core import parse_hex64, subkeys
key=parse_hex64("Enter 64-bit DES key in hex: ")
keys=subkeys(key)
print("Round keys:")
for i,k in enumerate(keys,1): print(f"K{i:02}: {k:012X}")
send_text(PORT,f"{key:016X}")
