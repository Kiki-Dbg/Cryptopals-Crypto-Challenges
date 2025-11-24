
from .byte_encoding import hex_to_bytes, b64_to_bytes, str_to_bytes

def _convert_text(text: str, action: str) -> bytes:
    action_map = {
        "hex_to_bytes": hex_to_bytes,
        "b64_to_bytes": b64_to_bytes,
        "str_to_bytes": str_to_bytes
    }
    if action in action_map:
        return action_map[action](text)
    else:
        print("byte convert error")
        exit()

def read_lines(name: str, action: str = 'str_to_bytes') -> list:
    with open(name, 'r') as file:
        lines = []
        for line in file:
            lines.append(_convert_text(line.strip(), action))
    return lines

def read_text(name: str, action: str = 'str_to_bytes') -> bytes:
    with open(name) as file:
        return _convert_text(file.read(), action)
