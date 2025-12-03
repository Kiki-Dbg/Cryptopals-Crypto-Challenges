# Crypto Challenges Set 1  
Is considered the qualifying set. With the aim of assessing if someone is ready to write code.  

The lessons and code from this set are important stepping stones to later attacks.   
##  
### Set 1: Challenge 1 — [Convert Hex to Base64](./chal_1.py)  
**Goal:**  
Convert a hex-encoded string to Base64 representation.  
**Summary:**  
Learn to decode hex into raw bytes and re-encode those bytes as Base64, a foundational skill required for all later Cryptopals exercises.  
**Reference:**  
[Set 1: Challenge 1](https://cryptopals.com/sets/1/challenges/1)  
**Example:**  
The string:  
```
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
```
Should produce:
```
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
```
**Cryptopals Rule:**  
Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
##  
### Set 1: Challenge 2 — [Fixed XOR](./chal_2.py)  
**Goal:**  
XOR two equal-length byte buffers.  
**Summary:**  
Learn bitwise XOR behaviour by decoding two hex strings, XORing them, and confirm the expected result.  
**Reference:**  
[Set 1: Challenge 2](https://cryptopals.com/sets/1/challenges/2)  
**Example:**  
The string:  
```
1c0111001f010100061a024b53535009181c
```
XOR'ed with
```
686974207468652062756c6c277320657965
```
Should produce:
```
746865206b696420646f6e277420706c6179
```
##  
### Set 1: Challenge 3 — [Single-byte XOR cipher](./chal_3.py)  
**Goal:**  
Decrypt a hex string that was encoded using a single-byte XOR key.  
**Summary:**  
This challenge introduces brute-forcing single-byte keys, scoring outputs by English-likeness, and recovery of both the key and plaintext.  
**Reference:**  
[Set 1: Challenge 3](https://cryptopals.com/sets/1/challenges/3)  
**Example:**  
The hex encoded string is:  
```
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
```
XOR'ed against a single byte
**Cryptopals Hint:**  
After this challenge, you have permission to make "ETAOIN SHRDLU" jokes.
##  
### Set 1: Challenge 4 — [Detect single-character XOR](./chal_4.py)  
**Goal:**  
find the 60-character string in the file that has been encrypted by single-character XOR.  
**Summary:**  
Extending single-byte XOR cracking by testing multiple strings and detecting which one decrypts into meaningful English.  
**Reference:**  
[Set 1: Challenge 4](https://cryptopals.com/sets/1/challenges/4)  
**Cryptopals Hint:**  
The code from challenge 3 should help  
##  
### Set 1: Challenge 5 — [Implement repeating-key XOR](./chal_5.py)  
**Goal:**  
Encrypt the string using repeating-key XOR with the key "ICE".  
**Summary:**  
Learning to apply repeating key cyclically across the plaintext using XOR. Gaining familiarity with repeating-key XOR is a building block in cryptography.  
**Reference:**  
[Set 1: Challenge 5](https://cryptopals.com/sets/1/challenges/5)  
**Example:**  
The string:  
```
Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal
```
XOR'ed with the key "ICE" should produce:
```
0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
```
##  
### Set 1: Challenge 6 — [Break repeating-key XOR](./chal_6.py)  
**Goal:**  
Decrypt a ciphertext that has been encrypted with repeating-key XOR by determining the key size, recovering the key, and producing the original plaintext.  
**Summary:**  
Learn Hamming-distance analysis to estimate the repeating-key length, and reconstruct the full XOR key and decrypt the message.  
**Reference:**  
[Set 1: Challenge 6](https://cryptopals.com/sets/1/challenges/6)  
**Example:**  
The Hamming distance is just the number of differing bits. The distance between:  
```
this is a test
```
and  
```
wokka wokka!!!
```
Is 37.  
**Cryptopals Hint:**  
This code will be surprisingly useful later on. Breaking repeating-key XOR ("Vigenere") is a "Crypto 101" thing. But "knowing how" is not the same as writing the code to "break it".
##  
### Set 1: Challenge 7 — [AES in ECB mode](./chal_7.py)  
**Goal:**  
Decrypt AES-128-ECB ciphertext (Base64-encoded) using the known key "YELLOW SUBMARINE".  
**Summary:**  
This challenge requires implementing AES-128-ECB decryption to prepare for later exercises that depend on understanding and manipulating AES ECB behavior.  
**Reference:**  
[Set 1: Challenge 7](https://cryptopals.com/sets/1/challenges/7)  
**Cryptopals Hint:**  
Don't use the OpenSSL command-line tool, the code created will come in handy.  
##  
### Set 1: Challenge 8 — [Detect AES in ECB mode](./chal_8.py)  
**Goal:**  
Detect which ciphertext in a list has been encrypted using AES-128 in ECB mode.  
**Summary:**  
This challenge requires identification of ECB-encrypted data by scanning each ciphertext for repeated 16-byte blocks, as statistical fingerprint of ECB mode.  
**Reference:**  
[Set 1: Challenge 8](https://cryptopals.com/sets/1/challenges/8)  
**Cryptopals Hint:**  
Remember the problem with ECB is that it is stateless and deterministic; the same 16 byte plaintext block will always produce the same 16 byte ciphertext.

