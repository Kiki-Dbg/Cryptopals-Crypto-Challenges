# Crypto Challenges Set 2: Block crypto

The first of several sets on block cipher cryptography.

This is bread-and-butter crypto, the kind you'll see implemented in most web software.

##

### Set 2: Challenge 2 — [Implement PKCS#7 padding](./chal_9.py)

**Goal:**  
Implement PKCS#7 padding to extend arbitrary-length plaintext so its size becomes an exact multiple of a given block length.  
**Summary:**  
This challenge introduces the PKCS#7 padding scheme used in block cipher modes, requiring you to append padding bytes where each byte’s value equals the number of padding bytes added.  
**Reference:**  
[Set 2: Challenge 9](https://cryptopals.com/sets/2/challenges/9)  
**Example:**  
The string:

```
YELLOW SUBMARINE
```

padded to 20 bytes would be:

```
YELLOW SUBMARINE\x04\x04\x04\x04
```

##
