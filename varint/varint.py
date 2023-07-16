import struct

def encode(integer):
  new_bits = []
  while integer > 0:
    current_byte = integer & 0x7f
    integer >>= 7
    if integer > 0: 
      current_byte |= 0x80 
    new_bits.append(current_byte)
  return bytes(new_bits)

def decode(bytes):
  if bytes == b'':
    return 0
  bits = []
  byte_array = bytearray(bytes)
  byte_array.reverse()
  for byte in byte_array:
     dropped = byte & 0x7f
     bits.append(bin(dropped)[2:].zfill(7))
  return int("".join(bits), 2)

def read_int_file(filename):
   f = open(filename, 'rb')
   return int.from_bytes(f.read())

if __name__ == '__main__':
    assert read_int_file("150.uint64") == 150
    assert read_int_file("maxint.uint64") == 18446744073709551615

    assert encode(150) == b'\x96\x01'
    assert decode(b'\x96\x01') == 150 

    assert decode(encode(read_int_file("1.uint64")))
    assert decode(encode(read_int_file("150.uint64")))
    assert decode(encode(read_int_file("maxint.uint64")))

    print("All tests pass")
    