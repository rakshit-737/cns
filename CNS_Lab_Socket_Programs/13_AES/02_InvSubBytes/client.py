import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.net import send_text
PORT=4132

from aes_core import hex_bytes, inv_sub_bytes
state=hex_bytes("Enter 16-byte state (32 hex digits): ")
out=inv_sub_bytes(state)
print("InvSubBytes output:",bytes(out).hex().upper())
send_text(PORT,state.hex())
