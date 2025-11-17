
from byte_conversion import *

def convert_bytes(text, action):
    action_map = {
        "hex_to_bytes": hex_to_bytes,
        "b64_to_bytes": b64_to_bytes,
        "str_to_bytes": str_to_bytes,
    }
    if action in action_map:
        return action_map[action](text)
    else:
        print("byte convert error")
        exit()

def get_file_lines(name, action='str_to_bytes'):
    with open(name, 'r') as file:
        lines = []
        for line in file:
            lines.append(convert_bytes(line.strip(), action))
    return lines

def get_file_text(name, action='str_to_bytes'):
    with open(name) as file:
        return convert_bytes(file.read(), action)
