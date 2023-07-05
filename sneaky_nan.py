import struct 

def conceal(message):
    if len(message) > 6:
        return "Sorry, your message is too long."

    byte_array = [0xff, 248 + len(message)]
    byte_array += bytes(message, 'utf-8')
    for _ in range(8 - len(byte_array)):
        byte_array.append(32)

    return struct.unpack('>d', bytes(byte_array))[0]

def extract(nan):
    byte_string = struct.pack('>d', nan)[2:]
    message = byte_string.decode('utf-8')

    return message.strip()