import hashlib
from common.net import send_text

PORT = 4143
message = input("Enter message to hash using SHA-512: ")

digest_preview = hashlib.sha512(message.encode("utf-8")).hexdigest()
print("Local SHA-512 digest:", digest_preview)
send_text(PORT, message)
print("Message sent to server for hashing.")
