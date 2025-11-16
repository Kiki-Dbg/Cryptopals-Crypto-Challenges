import sys
sys.path.insert(0, '../crytopals_lib')

from cryptopals_lib import *

########################################
#### code to complete the challange ####
########################################
text = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = "ICE"

text = str_to_bytes(text)
key = str_to_bytes(key)

ans = xor_repeat_key(key, text)

print(bytes_to_hex(ans))
