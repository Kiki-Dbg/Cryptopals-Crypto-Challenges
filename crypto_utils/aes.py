
from Cryptodome.Cipher import AES

from .block_logic import pkcs7_unpad, pkcs7_pad, BLOCK_SZ

########################################
#### AES related functions          ####
########################################

def encrypt_ecb(key: bytes, pt: bytes) -> bytes:
    raw = pkcs7_pad(pt)
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(raw)

def decrypt_ecb(key: bytes, ct: bytes) -> bytes:
        cipher = AES.new(key, AES.MODE_ECB)
        return pkcs7_unpad(cipher.decrypt(ct))

def detect_ecb(ct: bytes) -> tuple[int, int] | None:
    blocks = [ct[start:start+BLOCK_SZ] for start in range(0, len(ct), BLOCK_SZ)]
    seen = {}
    for i, block in enumerate(blocks):
        if block in seen:
            return seen[block], i
        seen[block] = i
    return None
