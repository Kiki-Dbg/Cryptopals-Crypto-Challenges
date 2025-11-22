
from Cryptodome.Cipher import AES

########################################
#### AES related functions          ####
########################################

def encrypt_AES_ECB(key, pt):
    raw = pad(pt)
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(raw)

def decrypt_AES_ECB(key, ct):
        cipher = AES.new(key, AES.MODE_ECB)
        return unpad(cipher.decrypt(ct))

block_sz=16

def pad(pt):
    return pt + bytes(([block_sz - len(pt) % block_sz]) * (block_sz - len(pt) % block_sz))

def unpad(ct):
    return ct[:-ord(ct[len(ct) - 1:])]

def detect_AES_ECB(ct):
    blocks = [ct[start:start+block_sz] for start in range(0, len(ct), block_sz)]
    seen = {}
    for i, block in enumerate(blocks):
        if block in seen:
            return seen[block], i
        seen[block] = i
    return None
