from base64 import b64decode, b64encode
from binascii import unhexlify, hexlify

########################################
#### convert datatypes to bytes     ####
########################################
def hex_to_bytes(input):
    #non-delimiter hex value as a string
    return unhexlify(input)

def b64_to_bytes(input):
    #base64 value as a string
    return b64decode(input)

def str_to_bytes(input):
    #python string datatype
    return bytes(input, "ascii")

def int_to_bytes(input):
    #single byte integer
    return input.to_bytes(1, 'big') 

########################################
## convert bytes to pretty datatypes  ##
########################################
def bytes_to_str(input):
    #python string datatype
    return input.decode("ascii")

def bytes_to_b64(input):
    #base64 value as a string
    return bytes_to_str(b64encode(input))
    
def bytes_to_hex(input):
    #non-delimiter hex value as a string
    return bytes_to_str(hexlify(input))

def bytes_to_int(input):
    #single byte integer
    return int.from_bytes(input, byteorder='big')
