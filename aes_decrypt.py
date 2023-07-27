#!/usr/bin/env python3

# Standard
import os
import sys

# PyPI
from Crypto.Cipher import AES

# Custom
from constant import BLOCK_SIZE, ENCRYPTED_FILE_NAME, KEY_FILE_NAME, PLAINTEXT_FILE_NAME
import utils


def main():
    aes_mode = AES.MODE_ECB
    print("AES-128-ECB decryption sample")

    if os.path.isfile(ENCRYPTED_FILE_NAME):
        print(f"Load ciphertext from file: {ENCRYPTED_FILE_NAME}")
        with open(ENCRYPTED_FILE_NAME, 'rb') as f:
            ciphertext = f.read()
            f.close()
    else:
        print(f"Ciphertext file: {ENCRYPTED_FILE_NAME} not found")
        sys.exit(1)
    print("Ciphertext:")
    utils.print_bytearray(ciphertext)

    if os.path.isfile(KEY_FILE_NAME):
        print(f"Load key from file: {KEY_FILE_NAME}")
        with open(KEY_FILE_NAME, 'rb') as f:
            key = f.read()
            f.close()
    else:
        print(f"Key file: {KEY_FILE_NAME} not found")
        sys.exit(1)
    print("Key:")
    utils.print_bytearray(key)

    cipher = AES.new(key, aes_mode)
    data = cipher.decrypt(ciphertext)
    utils.save_bytearray_to_file(data, PLAINTEXT_FILE_NAME)
    print("Data:")
    utils.print_bytearray(data)


main()
