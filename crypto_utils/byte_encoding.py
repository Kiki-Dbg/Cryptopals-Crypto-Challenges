from base64 import b64decode, b64encode
from binascii import unhexlify, hexlify

########################################
#### convert datatypes to bytes     ####
########################################
def hex_to_bytes(s: str) -> bytes:
    #non-delimiter hex value as a string
    return unhexlify(s)

def b64_to_bytes(s: str) -> bytes:
    #base64 value as a string
    return b64decode(s)

def str_to_bytes(s: str) -> bytes:
    #python string datatype
    return bytes(s, "ascii")

def int_to_bytes(n: int) -> bytes:
    #single byte integer
    return n.to_bytes(1, 'big') 

########################################
## convert bytes to pretty datatypes  ##
########################################
def bytes_to_str(b: bytes) -> str:
    #python string datatype
    return b.decode("ascii")

def bytes_to_b64(b: bytes) -> str:
    #base64 value as a string
    return bytes_to_str(b64encode(b))
    
def bytes_to_hex(b: bytes) -> str:
    #non-delimiter hex value as a string
    return bytes_to_str(hexlify(b))

def bytes_to_int(b: bytes) -> int:
    #single byte integer
    return int.from_bytes(b, byteorder='big')
