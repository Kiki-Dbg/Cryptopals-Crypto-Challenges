
from crypto_utils.byte_encoding import (
    hex_to_bytes,
    b64_to_bytes,
    str_to_bytes,
    int_to_bytes,
    bytes_to_str,
    bytes_to_hex,
    bytes_to_b64,
    bytes_to_int,
)

#run from root dir: python -m set_1.chal_1 

#example of data types
#x = "Hello World"	str 	
#x = 20			int 	
#x = b"Hello"		bytes 	
#x = bytearray(5)	bytearray 	

########################################
#### code to complete the challenge ####
########################################
test_text_hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
test_text_b64 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

# Hex to base64
print("hex to base64 test")
hex_raw = hex_to_bytes(test_text_hex)
str_b64 = bytes_to_b64(hex_raw)
print(str_b64)

# base64 to hex
print("base64 to hex test")
b64_raw = b64_to_bytes(test_text_b64)
str_hex = bytes_to_hex(b64_raw)
print(str_hex)

# string to bytes
print("test string to bytes")
str_bytes = str_to_bytes("Hello World!")
print(str_bytes)

# single byte int to bytes
print("test single byte int (int:50 = \\x32 = b'2') to bytes")
int_bytes = int_to_bytes(50)
print(int_bytes)
