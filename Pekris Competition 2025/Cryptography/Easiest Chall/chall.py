from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import os

key = b'p3kanr1stek_2025'
file_in = 'img.png'
file_out = 'encrypted_image.png.enc'

def encrypt_file(input_file, output_file, encryption_key):
    try:
        with open(input_file, 'rb') as f_in:
            plaintext = f_in.read()

        iv = get_random_bytes(16)
        cipher = AES.new(encryption_key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

        with open(output_file, 'wb') as f_out:
            f_out.write(ciphertext)
       
        print(f"File '{input_file}' encrypted to '{output_file}' successfully.")

    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_file}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    encrypt_file(file_in, file_out, key)
