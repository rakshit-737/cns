# CNS Lab Socket Programming — Python

This folder contains educational client/server socket programs for common Cryptography and Network Security lab experiments. Every experiment has separate Python files; AES and DES also have separate operation-level programs.

## Requirements
- Python 3.10 or newer recommended
- No third-party packages required
- Run commands from the **root `CNS_Lab_Socket_Programs` directory**, so `common.net` imports work.

## How to run any client/server pair
Open two PowerShell terminals in this folder.

Terminal 1:
```powershell
py path\to\server.py
```
Terminal 2:
```powershell
py path\to\client.py
```
For example:
```powershell
py 02_Caesar_Cipher\server.py
py 02_Caesar_Cipher\client.py
```
Start the server first. Each experiment uses its own localhost port.

## Experiment index
1. XOR stream cipher
2. Caesar cipher
3. Vigenère cipher
4. Vernam cipher
5. Playfair cipher
6. Hill cipher (2x2)
7. Rail Fence cipher
8. Row-column transposition (two columns)
9. RSA (small numeric demonstration)
10. Diffie–Hellman key exchange (toy parameters)
11. Diffie–Hellman MITM simulation (run Eve, then Bob, then Alice)
12. DES full encryption/decryption plus separate operation demonstrations
13. AES-128 full encryption/decryption plus separate operation demonstrations
14. ElGamal numeric encryption
15. DSS/DSA toy digital-signature signing and verification
16. MD5 hashing
17. SHA-512 hashing

## AES operation-wise programs
Inside `13_AES/`:
- `01_SubBytes`
- `02_InvSubBytes`
- `03_ShiftRows`
- `04_InvShiftRows`
- `05_MixColumns`
- `06_InvMixColumns`
- `07_AddRoundKey`
- `08_Key_Expansion`

Each operation folder contains `client.py`, `server.py`, and a short README. For the state, enter 16 bytes as 32 hexadecimal digits. Example state:
`00112233445566778899AABBCCDDEEFF`
For AddRoundKey, enter a second 16-byte round key.
For Key Expansion, enter a 16-byte AES-128 key (32 hex digits).

The full AES program takes a 16-byte key and 16-byte plaintext block, both as 32 hex digits. It sends the ciphertext to the server, which decrypts it.

## DES operation-wise programs
Inside `12_DES/`:
- `01_Initial_Permutation`
- `02_Key_Generation` (PC-1, C/D halves, left shifts, PC-2)
- `03_Expansion_Permutation`
- `04_SBox_Substitution`
- `05_Permutation_P`
- `06_DES_Encryption`
- `07_DES_Decryption`

DES inputs are 64-bit blocks/keys in hexadecimal (up to 16 hex digits). DES key generation prints all 16 round keys. Full DES encryption/decryption uses the standard IP, FP, expansion, P, PC-1, PC-2, shifts, and S-box tables.

## Security and academic notes
- These are classroom demonstrations, not production cryptography.
- DES is obsolete and insecure for modern use.
- Classical ciphers and small RSA/ElGamal/DSA parameters are not secure.
- The MITM program is a controlled localhost educational simulation, not a general-purpose attack tool.
- The simple Hill/Rail Fence/row-column examples are designed for teaching and may preserve padding characters such as `X`.
- AES operation demos accept raw state bytes in column-major order, matching AES's internal state representation.
- For actual secure systems, use a maintained cryptographic library and authenticated encryption.

## Troubleshooting
- `ModuleNotFoundError: common`: run the command from this root directory, not from inside the experiment folder.
- `Address already in use`: ensure you do not have another server running on that port.
- `ConnectionRefusedError`: start the corresponding server before the client.
- `ValueError` for AES input: enter exactly 32 hexadecimal digits for a 16-byte block/key.


## MD5 and SHA-512
- `16_MD5/`: client sends a message over a TCP socket; server calculates and prints its MD5 digest.
- `17_SHA512/`: client sends a message over a TCP socket; server calculates and prints its SHA-512 digest.
- Both use Python's built-in `hashlib`; no extra package is required.
- MD5 produces a 128-bit digest (32 hex characters); SHA-512 produces a 512-bit digest (128 hex characters).
- Hashing is one-way; it is not encryption. MD5 is broken for security-sensitive uses and is included only for the lab.
