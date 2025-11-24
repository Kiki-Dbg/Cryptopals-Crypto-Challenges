
from crypto_utils.io_utils import read_lines
from crypto_utils.xor import xor_bruteforce

########################################
#### code to complete the challange ####
########################################
total_candidates = []

lines = read_lines('./set_1/text_chal_4.txt', 'hex_to_bytes')

for line_no, test_text in enumerate(lines):
    best_line = xor_bruteforce(test_text)
    best_line["line"] = line_no
    total_candidates.append(best_line)

best_guess = sorted(total_candidates, key=lambda c: c['score'], reverse=True)[0]

print(best_guess)
