
from .byte_encoding import (
    hex_to_bytes,
    b64_to_bytes,
    str_to_bytes,
    int_to_bytes,
    bytes_to_str,
    bytes_to_hex,
    bytes_to_b64,
    bytes_to_int
)

from .xor import (
    xor_bytes,
    xor_bruteforce,
    xor_repeat,
    break_repeating_xor
)

from .io_utils import read_lines

from .lang_analysis import english_score

from .utils import hamming_dist

from .block_logic import pkcs7_unpad, pkcs7_pad

from .aes import decrypt_ecb, encrypt_ecb, detect_ecb

#from .aes import encrypt_ecb, decrypt_ecb, detect_ecb
#from .xor import xor_bytes, xor_repeating_key
#from .byte_encoding import (
#    hex_to_bytes, bytes_to_hex, b64_to_bytes, bytes_to_b64
#)

#from .io_utils import get_file_lines, get_file_text


# Define the __all__ variable
#__all__ = ["module1", "module2"]

# Import the submodules
#from . import module1
#from . import module2




#from aes import *

#from byte_encoding import *

#from lang_analysis import *

#from io_utils import *

#from xor import *
