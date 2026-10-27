import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.net import receive_text
PORT=4138

from aes_core import expand_key
key=bytes.fromhex(receive_text(PORT))
for i,rk in enumerate(expand_key(key)): print(f"Round key {i:02}: {bytes(rk).hex().upper()}")
