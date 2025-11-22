import sys
sys.path.insert(0, '../crytopals_lib')

from cryptopals_lib import *

########################################
#### code to complete the challange ####
########################################

test_text = get_file_lines("text_chal_8.txt", 'hex_to_bytes')

for line_no, line in enumerate(test_text, start=1):
    result = detect_AES_ECB(line)
    if None != result:
        print(f"found AES ECB at line {line_no}")
        print("The text from the line is:\n" + bytes_to_hex(line))
        break
