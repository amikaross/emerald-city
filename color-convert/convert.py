import sys
import re

def hex_to_rgb(hex_string):
    hex_string = hex_string.group()
    hexr, hexg, hexb = hex_string[1:3], hex_string[3:5], hex_string[5:]
    decr, decg, decb = int(hexr, 16), int(hexg, 16), int(hexb, 16)
    return f'rgb({decr} {decg} {decb})'


if __name__ == "__main__":
    text = sys.stdin.read()
    out = re.sub(r'#\w+', hex_to_rgb, text)
    sys.stdout.write(out)
