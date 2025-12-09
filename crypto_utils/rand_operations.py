
from typing import Sequence, TypeVar
from random import choice, randint

from .block_logic import BLOCK_SZ

########################################
###### entropy-related functions  ######
########################################

def random_key(key_size: int = BLOCK_SZ) -> bytes:
    return bytes(randint(0, 255) for _ in range(key_size))

def random_bool() -> bool:
    return choice([True, False])

def random_padding(min_len=5, max_len=10) -> bytes:
    pad_len = randint(min_len, max_len)
    return bytes(randint(0, 255) for _ in range(pad_len))

T = TypeVar("T")

def random_choice(values: Sequence[T]) -> T:
    return choice(values)