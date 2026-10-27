import sys
from pathlib import Path
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'common').is_dir())
sys.path.insert(0, str(ROOT))
from common.net import send_text
PORT = 4110

p=int(input("Enter prime p (demo e.g. 23): ")); g=int(input("Enter generator g (demo e.g. 5): "))
a=int(input("Enter private number a: "))
A=pow(g,a,p)
print("Your public value:",A)
send_text(PORT,f"{p} {g} {a} {A}")

