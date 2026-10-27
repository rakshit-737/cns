import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import send_text
PORT = 4108

msg="".join(ch for ch in input("Enter message: ").upper() if ch.isalpha())
if len(msg)%2: msg+="X"
cipher=msg[0::2]+msg[1::2]
print("Ciphertext:",cipher)
send_text(PORT,str(len(msg))+"\n"+cipher)

