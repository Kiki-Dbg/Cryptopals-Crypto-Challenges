
from typing import Literal

from .block_logic import BLOCK_SZ

from .rand_operations import random_key, random_bool, random_padding, random_choice

from .block_logic import pkcs7_pad

from .aes import encrypt_ecb, encrypt_cbc

########################################
######### AES specific oracles #########
########################################

def aes_rand_mode_oracle(pt: bytes, mode: Literal["ECB", "CBC"] | None = None) -> bytes:

    if mode is None:
        mode = random_choice(["ECB", "CBC"])

    key = random_key()

    pt_mod = pkcs7_pad(random_choice() + pt + random_padding())
    ct = b''

    if  mode == "ECB":
        ct = encrypt_ecb(key, pt_mod)
    elif mode == "CBC":
        iv = random_key()
        ct = encrypt_cbc(iv, key, pt_mod)

    return ct, mode

########################################
## Extended oracles with non AES data ##
########################################

def AES_rand_mode_oracle(pt):

    key = pseudorandom_key()

    prefix = bytes(randint(0, 255) for _ in range(randint(5, 10)))
    suffix= bytes(randint(0, 255) for _ in range(randint(5, 10)))
    pt_mod = pad(prefix + pt + suffix)
    ct = b''

    if select_options([True, False]):
        ct = encrypt_AES_ECB(key, pt_mod)
        mode = "ECB"
    else:
        iv = pseudorandom_key()
        ct = encrypt_AES_CBC(iv, key, pt_mod)
        mode = "CBC"
        
    mode = select_options(["ECB", "CBC", "NOT"])
    if mode == "ECB":
        ct = encrypt_AES_ECB(key, pt_mod)
    elif mode == "CBC":
        iv = pseudorandom_key()
        ct = encrypt_AES_CBC(iv, key, pt_mod)
    elif mode == "NOT":
        ct = bytes(randint(0, 255) for _ in range(len(pt_mod)+ randint(1, 5)))
    
    return ct, mode






########################################
######### detection functions ##########
########################################

def detect_ecb(ct: bytes) -> tuple[int, int] | None:
    blocks = [ct[start:start+BLOCK_SZ] for start in range(0, len(ct), BLOCK_SZ)]
    seen = {}
    for i, block in enumerate(blocks):
        if block in seen:
            return seen[block], i
        seen[block] = i
    return None