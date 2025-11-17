import sys
sys.path.insert(0, '../crytopals_lib')

from cryptopals_lib import *

########################################
#### XOR related functions          ####
########################################

def attack_repeat_key_xor(ciphertext, max_size):
    keysize = score_vigenere_key_size(ciphertext, max_size)

    key = b''
    message_parts = list()
    for i in range(keysize):
        part = xor_brute(ciphertext[i::keysize])
        key += part["key"]
        message_parts.append(part["plaintext"])

    message = bytearray()
    max_len = max(len(part) for part in message_parts)
    for a in range(max_len):
        for b in range(len(message_parts)):
                if a < len(message_parts[b]):
                    message.append(message_parts[b][a])

    return {'message':bytes(message), 'key':key}

########################################
#### misc crypto related functions  ####
########################################

def hamming_dist(a, b):
    return sum(bin(byte).count('1') for byte in xor_bytes(a,b))

def score_vigenere_key_size(ct, max_size):
    temp_score = 100
    value = 0
    for key_sz in range(2, max_size):

        nb_measurements = len(ct) // key_sz - 1
        score = 0
        for i in range(nb_measurements):
            #TODO fix this ugly line
            score += hamming_dist(ct[i*key_sz:(i*key_sz)+key_sz], ct[(i*key_sz)+ key_sz:(i*key_sz)+(2*key_sz)])

        score /= key_sz

        score /= nb_measurements
        if score < temp_score:
            value = key_sz
            temp_score = score

    return value

########################################
#### code to complete the challange ####
########################################
print("test hamming distance code")
print("'this is a test' and 'wokka wokka!!!' == 37")

test = hamming_dist(str_to_bytes('this is a test'),str_to_bytes('wokka wokka!!!'))
print(test)

print("Now to use the hamming code to find the key\n")
ciphertext = get_file_text("text_chal_6.txt", "b64_to_bytes")

result = attack_repeat_key_xor(ciphertext, 40)

print("key:",result["key"],'\n')
print('message:')
print(bytes_to_str(result["message"]))






