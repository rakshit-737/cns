import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import receive_text
from des_core import des
PORT=4112
cipher_text,key_text=receive_text(PORT).split()
plain=des(int(cipher_text,16),int(key_text,16),True)
print("Recovered plaintext:",f"{plain:016X}")
