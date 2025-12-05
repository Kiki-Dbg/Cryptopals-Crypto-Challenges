from crypto_utils.aes import encrypt_ecb, decrypt_ecb, pkcs7_pad, pkcs7_unpad

########################################
#### code to complete the challange ####
########################################

print("padding test for string of A's")
for i in range(20):
    text = b"A" * i
    print(pkcs7_pad(text))

print("test padding implementation for a string that is a multiple of 16 edge case")
key = b"1234567890123456"
pt0 = b""
pt1 = b"AAAAAAAAAAAAAAAA"
pt2 = b"AAAAAAAAAAAAAAAABBBBBBBBBBBBBBBB"

ct0 = encrypt_ecb(key, pkcs7_pad(pt0))
ct1 = encrypt_ecb(key, pkcs7_pad(pt1))
ct2 = encrypt_ecb(key, pkcs7_pad(pt2))

print(ct0)
print(ct1)
print(ct2)

print(pkcs7_unpad(decrypt_ecb(key, ct0)))
print(pkcs7_unpad(decrypt_ecb(key, ct1)))
print(pkcs7_unpad(decrypt_ecb(key, ct2)))
# TODO option for varible block size, and default the function to 16cd

print("test non-standard block size, still multiple of 16")
block_sz = 32

ct0 = encrypt_ecb(key, pkcs7_pad(pt0))
ct1 = encrypt_ecb(key, pkcs7_pad(pt1))
ct2 = encrypt_ecb(key, pkcs7_pad(pt2))

print(ct0)
print(ct1)
print(ct2)

print(pkcs7_unpad(decrypt_ecb(key, ct0)))
print(pkcs7_unpad(decrypt_ecb(key, ct1)))
print(pkcs7_unpad(decrypt_ecb(key, ct2)))

print("padding test for string of A's, block size = 5")
block_sz = 5
for i in range(20):
    text = b"A" * i
    print(pkcs7_pad(text))
