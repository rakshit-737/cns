import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import send_text
PORT = 4102

message = input("Enter message: ")
shift = int(input("Enter shift (0-25): ")) % 26
cipher = "".join(chr((ord(ch.upper()) - 65 + shift) % 26 + 65) if ch.isalpha() else ch for ch in message)
print("Ciphertext:", cipher)
send_text(PORT, str(shift) + "\n" + cipher)

