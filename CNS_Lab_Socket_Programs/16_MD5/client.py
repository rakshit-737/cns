from common.net import send_text

PORT = 4142
message = input("Enter message to hash using MD5: ")

digest_preview = __import__("hashlib").md5(message.encode("utf-8")).hexdigest()
print("Local MD5 digest:", digest_preview)
send_text(PORT, message)
print("Message sent to server for hashing.")
