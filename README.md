# Encryption and Decryption using Fernet:
This repository contains a Python script for encrypting and decrypting files using the Fernet symmetric encryption library. Fernet provides a secure and straightforward way to encrypt and decrypt data.

## How it Works
### Key Generation:
Run key_generator.py to generate a key.
The key is saved to a file named key.key.
### Encryption:
Place the file you want to encrypt in the project directory (e.g., photo.jpg).
Run encrypt_file.py to encrypt the file.
The encrypted file is saved as photo_encrypted.jpg.
### Decryption:
Run decrypt_file.py to decrypt the encrypted file (photo_encrypted.jpg).
The decrypted file is saved as photo_decrypted.jpg.
## Important Note:
Keep the key (key.key) secure. Losing the key will result in the inability to decrypt the encrypte
