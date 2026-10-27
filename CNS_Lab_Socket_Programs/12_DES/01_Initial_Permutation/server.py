import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.net import receive_text
PORT=4120

from des_core import permute, IP
v=int(receive_text(PORT),16)
print("Server confirms IP result:",f"{permute(v,IP,64):016X}")
