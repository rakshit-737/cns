import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import receive_text
PORT = 4140

p=23; x=6
C1,C2=map(int,receive_text(PORT).split())
shared=pow(C1,x,p)
message=(C2*pow(shared,-1,p))%p
print("Decrypted numeric message:",message)

