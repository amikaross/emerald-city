import struct 

def conceal(message):
    length = len(message)
    if length > 6:
        return "Sorry, your message is too long."

    byte_array = [0xff, 248 + length]
    byte_array += b'\x00' * (6 - length)
    byte_array += bytes(message, 'utf-8')

    return struct.unpack('>d', bytes(byte_array))[0]

def extract(nan):
    byte_string = struct.pack('>d', nan)
    length = byte_string[1] & 0x7
    string = byte_string[-length:]

    return string.decode('utf-8')




if __name__ == '__main__':
    cases = ('secret', 'test', 'what!')
    for case in cases:
        x = conceal(case)
        assert isinstance(x, float)
        assert repr(x) == 'nan'
        assert extract(x) == case