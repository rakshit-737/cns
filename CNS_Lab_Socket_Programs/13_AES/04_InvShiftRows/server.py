import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.net import receive_text
PORT=4134

from aes_core import inv_shift_rows
parts=receive_text(PORT).split("\n")
state=bytes.fromhex(parts[0])

out=inv_shift_rows(state)
print("InvShiftRows output:",bytes(out).hex().upper())
