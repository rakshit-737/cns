import hashlib
from common.net import receive_text

PORT = 4142
message = receive_text(PORT, "Waiting for message to hash...")
digest = hashlib.md5(message.encode("utf-8")).hexdigest()

print("Received message:", message)
print("MD5 digest:", digest)
