import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.net import send_text
PORT=4137

from aes_core import hex_bytes, add_round_key
state=hex_bytes("Enter 16-byte state (32 hex digits): ")
key=hex_bytes("Enter 16-byte round key (32 hex digits): ")
out=add_round_key(state, key)
print("AddRoundKey output:",bytes(out).hex().upper())
send_text(PORT,state.hex() + "\n" + key.hex())
