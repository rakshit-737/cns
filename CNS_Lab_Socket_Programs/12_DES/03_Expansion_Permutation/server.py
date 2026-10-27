import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.net import receive_text
PORT=4122

from des_core import permute, E
v=int(receive_text(PORT),16)
print("Expanded 48-bit value:",f"{permute(v,E,32):012X}")
