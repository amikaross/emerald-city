import struct

def encode(integer):
  if integer == 0:
    return b'\x00'
  new_bits = []
  while integer > 0:
    current_byte = integer & 0x7f
    integer >>= 7
    if integer > 0: 
      current_byte |= 0x80 
    new_bits.append(current_byte)
  return bytes(new_bits)

# def decode(bytes):
#   new_bits = []
#   byte_array = bytearray(bytes)
#   for byte in byte_array:
#      new_bits.append(bin(byte & 0x7f))
#   breakpoint()
#   return int("".join(new_bits), 2)


def decode(bytes):
  if bytes == b'\x00':
    return 0
  bits = []
  byte_array = bytearray(bytes)
  byte_array.reverse()
  for i in range(len(byte_array)):
     dropped = byte_array[i] & 0x7f
     bits.append(bin(dropped)[2:].zfill(7))
  return int("".join(bits), 2)

def read_int_file(filename):
   f = open(filename, 'rb')
   return int.from_bytes(f.read())
  #  return struct.unpack('>Q', f.read())[0]

if __name__ == '__main__':
    assert read_int_file("150.uint64") == 150
    assert read_int_file("maxint.uint64") == 18446744073709551615

    assert encode(150) == b'\x96\x01'
    assert decode(b'\x96\x01') == 150 

    assert decode(encode(1)) == 1

    for n in range(1 << 20):
      if n % 1000000 == 0:
        print(n)
      assert decode(encode(n)) == n
    