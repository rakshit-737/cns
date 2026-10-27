import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.net import receive_text
PORT=4137

from aes_core import add_round_key
parts=receive_text(PORT).split("\n")
state=bytes.fromhex(parts[0])
key=bytes.fromhex(parts[1])
out=add_round_key(state, key)
print("AddRoundKey output:",bytes(out).hex().upper())
