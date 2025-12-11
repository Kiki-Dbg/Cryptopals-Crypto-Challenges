from crypto_utils.byte_encoding import str_to_bytes, bytes_to_hex
from crypto_utils.rand_operations import random_key
from crypto_utils.block_logic import BLOCK_SZ
from crypto_utils.aes_oracles import aes_mode_detector, aes_rand_mode_oracle, random_block_oracle 

########################################
#### code to complete the challange ####
########################################

#random key test
print("tetsting the random key generator")
print(bytes_to_hex(random_key()))
print(bytes_to_hex(random_key()))

pt_1 = """
According to all known laws of aviation, there is no way a bee should be able to fly.
Its wings are too small to get its fat little body off the ground.
The bee, of course, flies anyway because bees don't care what humans think is impossible."""

pt_2 = """
Yellow, black. Yellow, black. Yellow, black. Yellow, black.
Ooh, black and yellow!
Let's shake it up a little.
Barry! Breakfast is ready!"""

pt = str_to_bytes(pt_1 + "A"*BLOCK_SZ*3 + pt_2)

results1 = []
for i in range(10):
    ct, mode = aes_rand_mode_oracle(pt)

    results1.append({
    "count": i + 1,
    "mode": mode,
    "ciphertext": ct
    })

for result in results1:
    aes_mode_detector(result["ciphertext"])
    print(result)
    print("")

print("testing random block oracle")
print("This test includes non AES encrypted data")

results2 = []
for i in range(20):
    ct, mode = random_block_oracle(pt)

    results2.append({
    "count": i + 1,
    "mode": mode,
    "ciphertext": ct
    })

for result in results2:
    aes_mode_detector(result["ciphertext"])
    print(result)
    print("")
