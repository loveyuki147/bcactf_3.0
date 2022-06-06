#!/usr/bin/env python3
import math
import binascii
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import bytes_to_long, long_to_bytes

def chunks(l, n):
    assert(len(l) % n == 0)
    for i in range(0, len(l), n):
        yield l[i:i+n]

FLAG_LEN = 72
M_SIZE = math.isqrt(FLAG_LEN * 8) # = 24

flag = input("What is your key? ")

assert(len(flag) == FLAG_LEN)

# turn flag into a matrix
inter_key = bin(int(flag.encode('ascii').hex(), 16))[2:].rjust(FLAG_LEN * 8, '0')
key = [[int(c) for c in l] for l in chunks(inter_key, M_SIZE)]
