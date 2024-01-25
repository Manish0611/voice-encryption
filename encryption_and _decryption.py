from cryptography.fernet import Fernet
key=Fernet.generate_key()
print(key)

#encryption
fernet=Fernet(key)
with open('key.key','wb') as filekey:
    filekey.write(key)
with open('key.key','rb') as filekey:
    key=filekey.read()
with open('photo.jpg','rb') as file:
    originalaudio=file.read()

encrypted=fernet.encrypt(originalaudio)
with open('photo encrypted.jpg','wb') as encrypted_file:
    encrypted_file.write(encrypted)
    # decryption
    fernet = Fernet(key)
    with open('photo encrypted.jpg', 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open('photo decrypted.jpg', 'wb') as dec_file:
        dec_file.write(decrypted)
