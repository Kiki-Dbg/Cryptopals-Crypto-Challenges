import sys
sys.path.insert(0, '../crytopals_lib')

from cryptopals_lib import *


########################################
## crypto and lanuage data and values ##
########################################
eng_chr_freq = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}

########################################
### engilish lang related functions  ###
########################################
def eng_score(input):
    score = 0
    for byte in input:
        score += eng_chr_freq.get(chr(byte).lower(), 0)
    return score

########################################
#### XOR related functions          ####
########################################
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

########################################
#### code to complete the challange ####
########################################
text = hex_to_bytes("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

ans = xor_brute(text)

print(ans)
