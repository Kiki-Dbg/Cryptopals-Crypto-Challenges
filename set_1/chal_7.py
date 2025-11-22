import sys
sys.path.insert(0, '../crytopals_lib')

from cryptopals_lib import *

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

########################################
#### code to complete the challange ####
########################################


ciphertext = get_file_text("text_chal_7.txt", 'b64_to_bytes')

key = "YELLOW SUBMARINE"
key = str_to_bytes(key)

print("AES ECB decrypt test")
print("##################################")
result = decrypt_AES_ECB(key, ciphertext)
print(bytes_to_str(result))

print("##################################")
print("AES ECB encrypt test")
test = encrypt_AES_ECB(key, result)
print(bytes_to_b64(test))







