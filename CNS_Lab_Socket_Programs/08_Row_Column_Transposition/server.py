import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import receive_text
PORT = 4108

n_text,cipher=receive_text(PORT).split("\n",1); n=int(n_text)
half=n//2; a=cipher[:half]; b=cipher[half:]
plain="".join(a[i]+b[i] for i in range(half))
print("Decrypted (trailing X may be padding):",plain)

