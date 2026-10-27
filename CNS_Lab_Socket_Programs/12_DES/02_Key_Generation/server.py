import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.net import receive_text
PORT=4121

from des_core import subkeys
key=int(receive_text(PORT),16)
keys=subkeys(key)
for i,k in enumerate(keys,1): print(f"K{i:02}: {k:012X}")
