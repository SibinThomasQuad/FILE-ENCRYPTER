from cryptography.fernet import Fernet
class secure:
    
    def generate_key(self,key_name):
        key = Fernet.generate_key()
        with open(key_name, 'wb') as filekey:
            filekey.write(key)
    
    def encrypt(self,key_file,target_file):
        with open(key_file, 'rb') as filekey:
            key = filekey.read()
            fernet = Fernet(key)
            with open(target_file, 'rb') as f:
                file = f.read()
        encrypt_file = fernet.encrypt(file)
        with open(target_file, 'wb') as encrypted_file:
            encrypted_file.write(encrypt_file)
            print('File is encrypted')
    
    def decrypt(self,key_file,target_file):
        with open(key_file, 'rb') as filekey:
            key = filekey.read()
        fernet = Fernet(key)
        with open(target_file, 'rb') as f:
            file = f.read()
        decrypt_file = fernet.decrypt(file)
        with open(target_file, 'wb') as decrypted_file:
            decrypted_file.write(decrypt_file)
        print('File is decrypted')
secure_obj = secure()
#secure_obj.generate_key('code.key')
secure_obj.decrypt('code.key','test.txt')
