
from .lang_analysis import english_score
from .utils import hamming_dist

def _score_key_size(ct: bytes, size: int) -> int:
    temp_score = 100
    value = 0
    for key_sz in range(2, size):

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

def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes([ x^y for (x,y) in zip(a, b)])

def xor_bruteforce(ct: bytes) -> dict:
    candidates = []
    for key_try in range(256):
        plaintext = xor_bytes(ct, bytes([key_try])*len(ct))
        score = english_score(plaintext)
        result = {  'key': bytes([key_try]),
                    'score': score,
                    'plaintext': plaintext }
        candidates.append(result)
    return sorted(candidates, key=lambda c: c['score'], reverse=True)[0]

def xor_repeat(key: bytes, text: bytes) -> bytes:
    keystream = key*(len(text)//len(key) + 1 )
    return xor_bytes(text, keystream)

def break_repeating_xor(ct: bytes, size: int) -> dict:
    keysize = _score_key_size(ct, size)

    key = b''
    message_parts = list()
    for i in range(keysize):
        part = xor_bruteforce(ct[i::keysize])
        key += part["key"]
        message_parts.append(part["plaintext"])

    message = bytearray()
    max_len = max(len(part) for part in message_parts)
    for a in range(max_len):
        for b in range(len(message_parts)):
                if a < len(message_parts[b]):
                    message.append(message_parts[b][a])

    return {'message':bytes(message), 'key':key}
