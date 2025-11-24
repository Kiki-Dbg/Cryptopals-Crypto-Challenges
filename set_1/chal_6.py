
from crypto_utils.byte_encoding import str_to_bytes, bytes_to_str
from crypto_utils.io_utils import read_text
from crypto_utils.utils import hamming_dist
from crypto_utils.xor import break_repeating_xor

########################################
#### code to complete the challange ####
########################################
print("test hamming distance code")
print("'this is a test' and 'wokka wokka!!!' == 37")

test = hamming_dist(str_to_bytes('this is a test'),str_to_bytes('wokka wokka!!!'))
print(test)

print("Now to use the hamming code to find the key\n")
ciphertext = read_text("./set_1/text_chal_6.txt", "b64_to_bytes")

result = break_repeating_xor(ciphertext, 40)

print("key:",result["key"],'\n')
print('message:')
print(bytes_to_str(result["message"]))
