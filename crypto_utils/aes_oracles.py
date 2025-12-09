
from typing import Literal

from .block_logic import BLOCK_SZ

from .rand_operations import random_key, random_padding, random_choice, random_int

from .block_logic import pkcs7_pad

from .aes import encrypt_ecb, encrypt_cbc

########################################
######### AES specific oracles #########
########################################

def aes_rand_mode_oracle(pt: bytes, mode: Literal["ECB", "CBC"] | None = None) -> tuple[bytes, str]:

    if mode is None:
        mode = random_choice(["ECB", "CBC"])

    key = random_key()

    pt_mod = pkcs7_pad(random_padding() + pt + random_padding())
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

def random_block_oracle(pt: bytes) -> tuple[bytes, str]:

    mode = random_choice(["ECB", "CBC", "NOT"])
    if mode == "ECB":
        ct = aes_rand_mode_oracle(pt, mode=mode)[0]
    elif mode == "CBC":
        ct = aes_rand_mode_oracle(pt, mode=mode)[0]
    elif mode == "NOT":
        length = random_int(5, 10) + len(pt) + random_int(5, 10)

        if length % BLOCK_SZ == 0:
            length += 1
        ct = bytes(random_int(0, 255) for _ in range(length))
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