
from crypto_utils.byte_encoding import str_to_bytes, str_to_bytes, bytes_to_hex
from crypto_utils.xor import xor_repeat

########################################
#### code to complete the challange ####
########################################
text = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = "ICE"

text = str_to_bytes(text)
key = str_to_bytes(key)

ans = xor_repeat(key, text)

print(bytes_to_hex(ans))
