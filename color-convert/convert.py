def hex_to_rgb(hex_string):
    hexr, hexg, hexb = hex_string[1:3], hex_string[3:5], hex_string[5:]
    decr, decg, decb = int(hexr, 16), int(hexg, 16), int(hexb, 16)
    return f'rgb({decr}, {decg}, {decb})'

if __name__ == '__main__':
    assert hex_to_rgb('#00ff00') == 'rgb(0, 255, 0)'
    print("All tests pass")