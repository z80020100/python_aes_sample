#!/usr/bin/env python3

# Standard
import os

# PyPI
from Crypto.Cipher import AES

# Custom
from constant import BLOCK_SIZE, ENCRYPTED_FILE_NAME, KEY_FILE_NAME
import utils


def main():
    aes_mode = AES.MODE_ECB
    key_length_bits = 128
    print("AES-128-ECB encryption sample")

    data_hex_string = "48656C6C6F2C20576F726C6421"  # Hello, World!
    data = utils.hex_string_to_bytearray(data_hex_string)
    # Aligne data to block boundary
    data = data + bytearray(BLOCK_SIZE - len(data) % BLOCK_SIZE)
    print("Data:")
    utils.print_bytearray(data)

    if os.path.isfile(KEY_FILE_NAME):
        print(f"Load key from file: {KEY_FILE_NAME}")
        with open(KEY_FILE_NAME, 'rb') as f:
            key = f.read()
            f.close()
    else:
        print(f"Key file: {KEY_FILE_NAME} not found")
        print(f"Generate a {key_length_bits}-bit key")
        key = utils.gen_random_key(key_length_bits)
        utils.save_bytearray_to_file(key, KEY_FILE_NAME)
    print("Key:")
    utils.print_bytearray(key)

    cipher = AES.new(key, aes_mode)
    ciphertext = cipher.encrypt(data)
    utils.save_bytearray_to_file(ciphertext, ENCRYPTED_FILE_NAME)
    print("Ciphertext:")
    utils.print_bytearray(ciphertext)


main()
