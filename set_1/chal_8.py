
from crypto_utils.byte_encoding import bytes_to_hex
from crypto_utils.io_utils import read_lines
from crypto_utils.aes_oracles import detect_ecb

########################################
#### code to complete the challange ####
########################################

test_text = read_lines("./set_1/text_chal_8.txt", 'hex_to_bytes')

for line_no, line in enumerate(test_text, start=1):
    result = detect_ecb(line)
    if None != result:
        print(f"found AES ECB at line {line_no}")
        print("The text from the line is:\n" + bytes_to_hex(line))
        break

