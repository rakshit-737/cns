import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.net import send_text
PORT=4138

from aes_core import hex_bytes, expand_key
key=hex_bytes("Enter AES-128 key (32 hex digits): ")
rounds=expand_key(key)
for i,rk in enumerate(rounds): print(f"Round key {i:02}: {bytes(rk).hex().upper()}")
send_text(PORT,key.hex())
