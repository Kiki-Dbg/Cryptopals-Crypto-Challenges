
from Cryptodome.Cipher import AES

from .block_logic import BLOCK_SZ

from .xor import xor_bytes

########################################
#### AES related functions          ####
########################################

def encrypt_ecb(key: bytes, pt: bytes) -> bytes:
    assert len(pt) % BLOCK_SZ == 0, "provided plaintext is not block aligned"
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pt)

def decrypt_ecb(key: bytes, ct: bytes) -> bytes:
        assert len(ct) % BLOCK_SZ == 0, "provided ciphertext is not block aligned"
        cipher = AES.new(key, AES.MODE_ECB)
        return cipher.decrypt(ct)

def encrypt_cbc(iv: bytes, key: bytes, pt: bytes) -> bytes:
    assert len(pt) % BLOCK_SZ == 0, "provided plaintext is not block aligned"
    chunked_pt = [pt[i:i+BLOCK_SZ] for i in range(0, len(pt), BLOCK_SZ)]
    xor_key = iv
    ct = b''
    for chunk in chunked_pt:
        data = xor_bytes(xor_key, chunk)
        xor_key = encrypt_ecb(key, data)
        ct += xor_key
    return ct

def decrypt_cbc(iv: bytes, key: bytes, ct: bytes) -> bytes:
    assert len(ct) % BLOCK_SZ == 0, "provided ciphertext is not block aligned"
    chunked_ct = [ct[i:i+BLOCK_SZ] for i in range(0, len(ct), BLOCK_SZ)]
    xor_key = iv
    pt = b''
    for chunk in chunked_ct:
        data = decrypt_ecb(key, chunk)
        pt += xor_bytes(xor_key, data)
        xor_key = chunk
    return pt