import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import send_text
PORT = 4103

message = input("Enter alphabetic message: ").upper()
key = input("Enter alphabetic key: ").upper()
if not key.isalpha() or not message.isalpha():
    raise SystemExit("Use letters only for this simple lab version.")
cipher = "".join(chr((ord(ch)-65 + ord(key[i % len(key)])-65) % 26 + 65) for i,ch in enumerate(message))
print("Ciphertext:", cipher)
send_text(PORT, key + "\n" + cipher)

