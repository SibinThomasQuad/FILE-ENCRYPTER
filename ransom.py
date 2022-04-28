from cryptography.fernet import Fernet
import os
                
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

class Directory:
    
    secure_obj = secure()
    
    def all(self,root,key_name):
        self.secure_obj.generate_key(key_name)
        for path, subdirs, files in os.walk(root)   : 
            for name in files                       : 
                file_path                           = os.path.join(path, name)
                print(file_path)
                self.secure_obj.encrypt(key_name,file_path)

dir_obj = Directory()
dir_obj.all('git','a234rt.key')