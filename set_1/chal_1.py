from base64 import b64decode, b64encode
from binascii import unhexlify, hexlify

#example of data types
#x = "Hello World"	str 	
#x = 20			int 	
#x = b"Hello"		bytes 	
#x = bytearray(5)	bytearray 	

########################################
#### convert datatypes to bytes     ####
########################################
def hex_bytes(input):
    #non-delimiter hex value as a string
    print(type(input))
    output = unhexlify(input)
    print(type(output))
    return output

def b64_bytes(input):
    #base64 value as a string
    print(type(input))
    output = b64decode(input)
    print(type(output))
    return output

def str_bytes(input):
    #python string datatype
    print(type(input))
    output = bytes(input, "ascii")
    print(type(output))
    return output

def int_bytes(input):
    #single byte integer
    print(type(input))
    output = input.to_bytes(1, 'big')
    print(type(output))
    return output  

########################################
## convert bytes to pretty datatypes  ##
########################################
def bytes_str(input):
    #python string datatype
    return input.decode("ascii")

def bytes_b64(input):
    #base64 value as a string
    return bytes_str(b64encode(input))
    
def bytes_hex(input):
    #non-delimiter hex value as a string
    return bytes_str(hexlify(input))

def bytes_int(input):
    #single byte integer
    return int.from_bytes(input, byteorder='big')

########################################
#### code to complete the challenge ####
########################################
test_text_hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
test_text_b64 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

# Hex to base64
print("hex to base64 test")
hex_raw = hex_bytes(test_text_hex)
str_b64 = bytes_b64(hex_raw)
print(str_b64)

# base64 to hex
print("base64 to hex test")
b64_raw = b64_bytes(test_text_b64)
str_hex = bytes_hex(b64_raw)
print(str_hex)

# string to bytes
print("test string to bytes")
str_bytes = str_bytes("Hello World!")
print(str_bytes)

# single byte int to bytes
print("test single byte int (int:50 = \\x32 = b'2') to bytes")
int_bytes = int_bytes(50)
print(int_bytes)
