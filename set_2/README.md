# Crypto Challenges Set 2: Block crypto
The first of several sets on block cipher cryptography.

This is bread-and-butter crypto, the kind you'll see implemented in most web software.  
##  
### Set 2: Challenge 9 — [Implement PKCS#7 padding](./chal_9.py)  
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
### Set 2: Challenge 10 — [Implement CBC mode](./chal_10.py)

**Goal:**  
Implement AES encryption and decryption in CBC mode using the existing ECB and XOR functions.  
**Summary:**  
This challenge teaches how CBC mode chains blocks by XORing each plaintext block with the previous ciphertext block (or IV for the first block) before encrypting, requiring to build full CBC logic manually on top of your ECB implementation.  
**Reference:**  
[Set 2: Challenge 10](https://cryptopals.com/sets/2/challenges/10)  
**Example:**  
The chellenge text file is encrypted with the key:

```
YELLOW SUBMARINE
```

Using the following as the IV:

```
all ASCII 0 (\x00\x00\x00 &c)
```
**Cryptopals Rule:**  
Don't cheat! Do not use OpenSSL's CBC code to do CBC mode, even to verify your results. What's the point of even doing this stuff if you aren't going to learn from it.
##