import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import receive_text
PORT = 4102

shift_text, cipher = receive_text(PORT).split("\n", 1)
shift = int(shift_text)
plain = "".join(chr((ord(ch) - 65 - shift) % 26 + 65) if ch.isalpha() else ch for ch in cipher)
print("Decrypted message:", plain)

