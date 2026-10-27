import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.net import send_text
PORT=4126

from des_core import parse_hex64, des
cipher=parse_hex64("Enter 64-bit ciphertext block in hex: ")
key=parse_hex64("Enter 64-bit key in hex: ")
plain=des(cipher,key,True)
print("Decrypted plaintext:",f"{plain:016X}")
send_text(PORT,f"{cipher:016X} {key:016X}")
