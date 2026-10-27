import hashlib
from common.net import receive_text

PORT = 4143
message = receive_text(PORT, "Waiting for message to hash...")
digest = hashlib.sha512(message.encode("utf-8")).hexdigest()

print("Received message:", message)
print("SHA-512 digest:", digest)
