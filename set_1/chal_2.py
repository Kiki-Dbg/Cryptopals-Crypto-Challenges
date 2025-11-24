
from crypto_utils.byte_encoding import hex_to_bytes, bytes_to_hex
from crypto_utils.xor import xor_bytes





########################################
#### code to complete the challange ####
########################################
str1 = "1c0111001f010100061a024b53535009181c"
str2 = "686974207468652062756c6c277320657965"

str1 = hex_to_bytes(str1)
str2 = hex_to_bytes(str2)
ans = xor_bytes(str1, str2)

print(bytes_to_hex(ans))
