import struct

def encode(integer):
  bit_string = bin(integer)[2:]
  num_pads = 7 - (len(bit_string) % 7)
  padded = bit_string.zfill(num_pads + len(bit_string))
  split = [padded[i:i+7] for i in range(0, len(padded), 7)]
  for i in range(len(split)):
      if i != len(split) - 1:
        split[i] = '0' + split[i] 
      else: 
         split[i] = '1' + split[i]
  split.reverse()
  ints = list(map(lambda x: int(x, 2), split))
  return bytes(ints)

def decode(bytes):
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

    # for n in range(1 << 30):
    #   assert decode(encode(n)) == n
    