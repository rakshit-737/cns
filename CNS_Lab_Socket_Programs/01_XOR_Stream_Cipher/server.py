import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import receive_text
PORT = 4101

payload = receive_text(PORT)
key, cipher = payload.split("\n", 1)
raw = bytes.fromhex(cipher)
plain = "".join(chr(byte ^ ord(key)) for byte in raw)
print("Decrypted message:", plain)

