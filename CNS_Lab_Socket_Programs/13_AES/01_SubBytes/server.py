import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.net import receive_text
PORT=4131

from aes_core import sub_bytes
parts=receive_text(PORT).split("\n")
state=bytes.fromhex(parts[0])

out=sub_bytes(state)
print("SubBytes output:",bytes(out).hex().upper())
