import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import send_text
PORT = 4101

message = input("Enter message: ")
key = input("Enter one-character key: ")
if len(key) != 1:
    raise SystemExit("Key must be exactly one character.")
cipher = bytes([ord(ch) ^ ord(key) for ch in message]).hex()
print("Ciphertext (hex):", cipher)
send_text(PORT, key + "\n" + cipher)

