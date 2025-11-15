import sys
sys.path.insert(0, '../crytopals_lib')

from cryptopals_lib import *

########################################
#### code to complete the challange ####
########################################
total_candidates = []

lines = get_file_lines('text_chal_4.txt', 'hex_to_bytes')

for line_no, test_text in enumerate(lines):
    best_line = xor_brute(test_text)
    best_line["line"] = line_no
    total_candidates.append(best_line)

best_guess = sorted(total_candidates, key=lambda c: c['score'], reverse=True)[0]

print(best_guess)
