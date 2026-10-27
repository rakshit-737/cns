import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.net import receive_text
PORT=4126

from des_core import des
cipher_text,key_text=receive_text(PORT).split()
print("Server decrypted plaintext:",f"{des(int(cipher_text,16),int(key_text,16),True):016X}")
