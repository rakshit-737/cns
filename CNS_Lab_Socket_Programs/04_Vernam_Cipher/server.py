import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import receive_text
PORT = 4104

key, cipher = receive_text(PORT).split("\n", 1)
plain = "".join(chr(((ord(a)-65) ^ (ord(b)-65)) % 26 + 65) for a,b in zip(cipher,key))
print("Decrypted message:", plain)

