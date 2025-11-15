
from language_analysis import *

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
