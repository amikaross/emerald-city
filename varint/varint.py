import struct

def encode(integer):
  new_bits = []
  while integer > 0:
    current_chunk = integer & 0x7f
    integer >>= 7
    if integer > 0: 
      current_chunk|= 0x80 
    new_bits.append(current_chunk)
  return bytes(new_bits)

def decode(bytes):
  num = 0
  for byte in reversed(bytes):
    num <<= 7
    num |= (byte & 0x7f)
  return num

def read_int_file(filename):
   f = open(filename, 'rb')
   return int.from_bytes(f.read())

if __name__ == '__main__':
    assert read_int_file("150.uint64") == 150
    assert read_int_file("maxint.uint64") == 18446744073709551615

    assert encode(150) == b'\x96\x01'
    assert decode(b'\x96\x01') == 150 
    assert encode(18446744073709551615) == b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01'
    assert decode(b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01') == 18446744073709551615

    assert decode(encode(read_int_file("1.uint64")))
    assert decode(encode(read_int_file("150.uint64")))
    assert decode(encode(read_int_file("maxint.uint64")))

    print("All tests pass")
    