import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.net import receive_text
PORT=4133

from aes_core import shift_rows
parts=receive_text(PORT).split("\n")
state=bytes.fromhex(parts[0])

out=shift_rows(state)
print("ShiftRows output:",bytes(out).hex().upper())
