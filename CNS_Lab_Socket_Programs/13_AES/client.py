import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import send_text
from aes_core import hex_bytes, encrypt_block
PORT=4130
key=hex_bytes("Enter AES-128 key (32 hex digits): ")
block=hex_bytes("Enter plaintext block (32 hex digits): ")
cipher=encrypt_block(block,key)
print("Ciphertext:",cipher.hex().upper())
send_text(PORT,key.hex()+"\n"+cipher.hex())
