import struct 

def conceal(message):
    if len(message) > 6:
        return "Sorry, your message is too long."

    byte_array = [0b11111111, 0b11111111]
    byte_array += bytes(message, 'utf-8')
    for _ in range(8 - len(byte_array)):
        byte_array.append(32)

    x = struct.unpack('>d', bytes(byte_array))[0]

    return x


def extract(nan):
    full_byte_string = struct.pack('>d', nan)
    byte_string = full_byte_string[2:]
    message = byte_string.decode('utf-8')

    return message.strip()