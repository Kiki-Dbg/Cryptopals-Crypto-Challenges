# Crypto Challenges Set 1  
Is considered the qualifying set. With the aim of assessing if someone is ready to write code.  

The lessons and code from this set are important stepping stones to later attacks.   
##  
### Set 1: Challenge 1 — [Convert Hex to Base64](./chal_1.py)  
**Goal:**  
Convert a hex string into Base64 string.  
**Summary:**  
Learn basic encoding conversion between hex and Base64.  
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
XOR two fixed length buffers.  
**Summary:**  
Learn logic operators on byte arrays.  
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
decrypt the message that is XOR'ed against a single byte.  
**Summary:**  
Learning English plaintext character frequency and evaluation.  
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
find the 60-character string in the file that has been encrypted by single-character XOR 
**Summary:**  
Finding encoded text in a file  
**Reference:**  
[Set 1: Challenge 4](https://cryptopals.com/sets/1/challenges/4)  
**Cryptopals Hint:**  
The code from challenge 3 should help




##  
### Set 1: Challenge 5 — [Implement repeating-key XOR](./chal_5.py)  
**Goal:**  
Encrypt the string using repeating-key XOR with the key "ICE".  
**Summary:**  
Learning how to use a repeating key to encrypt data.  
**Reference:**  
[Set 1: Challenge 5](https://cryptopals.com/sets/1/challenges/5)  
**Example:**  
The string:  
```
Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal
```
XOR'ed with the key "ICE" will  Should produce:
```
0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
```


