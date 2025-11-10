# Crypto Challenge Set 1
Is considered the qualifying set. With the aim of assessing if someone is ready to write code.

The lessons and code from this set are important stepping stones to later attacks.
### Challenges
-----------
### Set 1: Challenge 1 — [Convert Hex to Base64](./set_1/chal_1.py)
**Goal:**  
Convert a hex string into Base64 string.
**Summary:**  
Learn basic encoding conversion between hex and Base64.
**Reference:**  
[Cryptopals Set 1, Challenge 1](https://cryptopals.com/sets/1/challenges/1)
**Example**
The string:
```
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
```
Should produce:
```
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
```
**Cryptopals Rule**
Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.










