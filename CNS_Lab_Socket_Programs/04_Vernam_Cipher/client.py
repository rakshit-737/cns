import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import send_text
PORT = 4104

message = input("Enter message (A-Z only): ").upper()
key = input("Enter same-length key (A-Z only): ").upper()
if not message.isalpha() or len(message) != len(key) or not key.isalpha():
    raise SystemExit("Message and key must be alphabetic and have equal length.")
cipher = "".join(chr(((ord(a)-65) ^ (ord(b)-65)) % 26 + 65) for a,b in zip(message,key))
print("Ciphertext:", cipher)
send_text(PORT, key + "\n" + cipher)

