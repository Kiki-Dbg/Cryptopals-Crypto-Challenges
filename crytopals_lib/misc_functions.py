
from xor_functions import *

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
#### XOR related functions          ####
########################################
def xor_bytes(a, b):
    return bytes([ x^y for (x,y) in zip(a, b)])

def xor_brute(ciphertext):
    candidates = []
    for key_try in range(256):
        plaintext = xor_bytes(ciphertext, bytes([key_try])*len(ciphertext))
        score = eng_score(plaintext)
        result = {  'key': bytes([key_try]),
                    'score': score,
                    'plaintext': plaintext }
        candidates.append(result)
    return sorted(candidates, key=lambda c: c['score'], reverse=True)[0]

def xor_repeat_key(key, text):
    keystream = key*(len(text)//len(key) + 1 )
    return xor_bytes(text, keystream)

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
