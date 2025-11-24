
########################################
#### misc crypto related functions  ####
########################################

def hamming_dist(a: bytes, b: bytes) -> int:
    from .xor import xor_bytes
    return sum(bin(byte).count('1') for byte in xor_bytes(a,b))
