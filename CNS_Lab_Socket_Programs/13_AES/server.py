import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import receive_text
from aes_core import decrypt_block
PORT=4130
key_text,cipher_text=receive_text(PORT).split("\n",1)
plain=decrypt_block(bytes.fromhex(cipher_text),bytes.fromhex(key_text))
print("Decrypted plaintext (hex):",plain.hex().upper())
try: print("As UTF-8:",plain.decode("utf-8"))
except UnicodeDecodeError: print("Plaintext is binary data, not valid UTF-8.")
