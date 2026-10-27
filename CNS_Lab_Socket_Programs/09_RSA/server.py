import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import receive_text
PORT = 4109

key_text,c_text=receive_text(PORT).split("\n",1)
n,d=map(int,key_text.split()); c=int(c_text)
print("Decrypted message:",pow(c,d,n))

