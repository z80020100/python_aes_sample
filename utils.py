# PyPI
from Crypto.Random import get_random_bytes


def gen_random_key(key_length_bits):
    return get_random_bytes(key_length_bits // 8)


def hex_string_to_bytearray(hex_string):
    return bytearray.fromhex(hex_string)


def save_bytearray_to_file(bytearray, filename):
    with open(filename, 'wb') as f:
        f.write(bytearray)
        f.close()


def print_bytearray(bytearray):
    for x in bytearray:
        print(f"{x:02X}", end=' ')
    print("")
