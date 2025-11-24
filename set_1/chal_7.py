
from crypto_utils.byte_encoding import str_to_bytes, bytes_to_str, bytes_to_b64
from crypto_utils.io_utils import read_text
from crypto_utils.aes import decrypt_ecb, encrypt_ecb

########################################
#### code to complete the challange ####
########################################

ciphertext = read_text("./set_1/text_chal_7.txt", 'b64_to_bytes')

key = "YELLOW SUBMARINE"
key = str_to_bytes(key)

print("AES ECB decrypt test")
print("##################################")
result = decrypt_ecb(key, ciphertext)
print(bytes_to_str(result))

print("##################################")
print("AES ECB encrypt test")
test = encrypt_ecb(key, result)
print(bytes_to_b64(test))
