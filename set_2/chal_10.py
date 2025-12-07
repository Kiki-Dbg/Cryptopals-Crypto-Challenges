from crypto_utils.byte_encoding import str_to_bytes, bytes_to_str, bytes_to_hex
from crypto_utils.io_utils import read_text
from crypto_utils.block_logic import pkcs7_pad, pkcs7_unpad
from crypto_utils.aes import encrypt_cbc, decrypt_cbc

########################################
#### code to complete the challange ####
########################################

key = str_to_bytes("aaaaaaaaaaaaaaaa")
iv = str_to_bytes("bbbbbbbbbbbbbbbb")

text0 = str_to_bytes("1234567")
test0 = encrypt_cbc(iv, key, pkcs7_pad(text0))
print("AES CBC test")
print(bytes_to_hex(test0))
print("should equal, source cyberchef")
print("ba1c547bbfe4c919bf0c2d118ac764e4")

text1 = str_to_bytes("1234567890123456")
test1 = encrypt_cbc(iv, key, pkcs7_pad(text1))
print(bytes_to_hex(test1))
print("should equal, source cyberchef")
print("a9519acf1b86107a930012023befd614b8cd6791ea4a66b2d6c33e4b0240f51c")

text2 = str_to_bytes("123456789012345612345")
test2 = encrypt_cbc(iv, key, pkcs7_pad(text2))
print(bytes_to_hex(test2))
print("should equal, source cyberchef")
print("a9519acf1b86107a930012023befd614086e3a0eb9b094bb1e95c3a5988e5e01")

text3 = str_to_bytes("12345678901234561234567890123456")
test3 = encrypt_cbc(iv, key, pkcs7_pad(text3))
print(bytes_to_hex(test3))
print("should equal, source cyberchef")
print("a9519acf1b86107a930012023befd6141a173181ab6d98b86b4893f7f6ecfe3a31ea0989bcd19a88a0be4ec1bd8eba71")

print("test decrypt function")
test0 = pkcs7_unpad(decrypt_cbc(iv, key, test0))
print(bytes_to_str(test0))
print("should equal, source cyberchef")
print("1234567")

test1 = pkcs7_unpad(decrypt_cbc(iv, key, test1))
print(bytes_to_str(test1))
print("should equal, source cyberchef")
print("1234567890123456")

test2 = pkcs7_unpad(decrypt_cbc(iv, key, test2))
print(bytes_to_str(test2))
print("should equal, source cyberchef")
print("123456789012345612345")

test3 = pkcs7_unpad(decrypt_cbc(iv, key, test3))
print(bytes_to_str(test3))
print("should equal, source cyberchef")
print("12345678901234561234567890123456")

print("")
print("test decryption of the file:")
#with open("2_10.txt") as file:
#        ciphertext = b64_to_bytes(file.read())


key = str_to_bytes("YELLOW SUBMARINE")
iv = b'\x00'*16

test_file = pkcs7_unpad(decrypt_cbc(iv, key, read_text("./set_2/text_chal_10.txt", "b64_to_bytes")))
print(bytes_to_str(test_file))
