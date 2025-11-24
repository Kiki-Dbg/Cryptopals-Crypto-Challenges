
BLOCK_SZ=16

def pkcs7_pad(pt: bytes) -> bytes:
    return pt + bytes(([BLOCK_SZ - len(pt) % BLOCK_SZ]) * (BLOCK_SZ - len(pt) % BLOCK_SZ))

def pkcs7_unpad(ct: bytes) -> bytes:
    return ct[:-ord(ct[len(ct) - 1:])]
