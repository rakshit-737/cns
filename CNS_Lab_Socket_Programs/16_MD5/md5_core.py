"""MD5 implemented from scratch. No hashlib or external crypto library."""
import math
MASK = 0xFFFFFFFF
S = ([7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 +
     [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4)
K = [int(abs(math.sin(i + 1)) * (1 << 32)) & MASK for i in range(64)]

def left_rotate(x, amount):
    """Rotate a 32-bit word left."""
    x &= MASK
    return ((x << amount) | (x >> (32 - amount))) & MASK

def F(b, c, d):
    return (b & c) | ((~b) & d)

def G(b, c, d):
    return (b & d) | (c & (~d))

def H(b, c, d):
    return b ^ c ^ d

def I(b, c, d):
    return c ^ (b | (~d))

def pad_message(message: bytes) -> bytes:
    """Append 1 bit, zeros to 448 mod 512, then original bit length (64-bit LE)."""
    original_bit_length = (len(message) * 8) & 0xFFFFFFFFFFFFFFFF
    padded = bytearray(message)
    padded.append(0x80)
    while (len(padded) % 64) != 56:
        padded.append(0)
    padded += original_bit_length.to_bytes(8, "little")
    return bytes(padded)

def md5(message: bytes) -> str:
    # Initial state words from the MD5 specification
    A, B, C, D = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476
    functions = (F, G, H, I)

    padded = pad_message(message)
    for offset in range(0, len(padded), 64):
        block = padded[offset:offset + 64]
        M = [int.from_bytes(block[j:j+4], "little") for j in range(0, 64, 4)]
        a, b, c, d = A, B, C, D

        for i in range(64):
            round_no = i // 16
            if round_no == 0:
                g = i
            elif round_no == 1:
                g = (5 * i + 1) % 16
            elif round_no == 2:
                g = (3 * i + 5) % 16
            else:
                g = (7 * i) % 16

            f = functions[round_no](b, c, d) & MASK
            temp = (a + f + K[i] + M[g]) & MASK
            temp = left_rotate(temp, S[i])
            temp = (b + temp) & MASK

            # MD5's working-register rotation
            a, b, c, d = d, temp, b, c

        A = (A + a) & MASK
        B = (B + b) & MASK
        C = (C + c) & MASK
        D = (D + d) & MASK

    # MD5 serializes each state word little-endian
    raw = b"".join(x.to_bytes(4, "little") for x in (A, B, C, D))
    return raw.hex()

if __name__ == "__main__":
    text = input("Enter message: ")
    print("MD5:", md5(text.encode("utf-8")))
