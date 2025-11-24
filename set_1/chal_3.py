
from crypto_utils.byte_encoding import hex_to_bytes
from crypto_utils.xor import xor_bruteforce

########################################
#### code to complete the challange ####
########################################
text = hex_to_bytes("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

ans = xor_bruteforce(text)

print(ans)
