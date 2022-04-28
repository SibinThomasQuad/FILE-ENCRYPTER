from cryptography.fernet import Fernet
import os
                
class secure                                              : 
    
    def generate_key(self,key_name)                       : 
        key                                               = Fernet.generate_key()
        with open(key_name, 'wb') as filekey              : 
            filekey.write(key)
        print("[+] Key generated "+key_name)
    
    def encrypt(self,key_file,target_file)                : 
        with open(key_file, 'rb') as filekey              : 
            key                                           = filekey.read()
            fernet                                        = Fernet(key)
            with open(target_file, 'rb') as f             : 
                file                                      = f.read()
        encrypt_file                                      = fernet.encrypt(file)
        with open(target_file, 'wb') as encrypted_file    : 
            encrypted_file.write(encrypt_file)
            print('[+][STATUS][File is encrypted]')
    
    def decrypt(self,key_file,target_file)                : 
        with open(key_file, 'rb') as filekey              : 
            key                                           = filekey.read()
        fernet                                            = Fernet(key)
        with open(target_file, 'rb') as f                 : 
            file                                          = f.read()
        decrypt_file                                      = fernet.decrypt(file)
        with open(target_file, 'wb') as decrypted_file    : 
            decrypted_file.write(decrypt_file)
        print('[+][STATUS][File is decrypted]')

class Directory                                           : 
    
    secure_obj                                            = secure()
    
    def all(self,root,key_name,task)                      : 
        for path, subdirs, files in os.walk(root)         : 
            for name in files                             : 
                file_path                                 = os.path.join(path, name)
                print("[+]['WORKING FILE']["+file_path+"]")
                if(task == 'encrypt'):
                    self.secure_obj.encrypt(key_name,file_path)
                if(task == 'decrypt'):
                    self.secure_obj.decrypt(key_name,file_path)

def main()                                                : 
    dir_obj                                               = Directory()
    secure_obj                                            = secure()
    print("[1] [Generate Key]")
    print("[2] [Encrypt all files in a folder]")
    print("[3] [Decrypt all files in a folder]")
    print("[4] [Encrypt a single file]")
    print("[5] [Decrypt a single file]")
    print("[0] [Exit]\n")
    task                                                  = input("Choose Operation : ")
    if(task == '0'):
        quit()
    if(task == '1'):
        key_name                                          = input("Enter keyname : ")
        secure_obj.generate_key(key_name)
    if(task == '2'):
        key_name                                          = input("Enter keyname : ")
        folder_name                                       = input("Enter Folder name (Full path) : ")
        dir_obj.all(folder_name,key_name,'encrypt')
    if(task == '3'):
        key_name                                          = input("Enter keyname : ")
        folder_name                                       = input("Enter Folder name (Full path) : ")
        dir_obj.all(folder_name,key_name,'decrypt')
    if(task == '4'):
        key_name                                          = input("Enter keyname : ")
        target_file                                       = input("Enter File name (Full path) : ")
        secure_obj.encrypt(key_name,target_file)
    if(task == '5'):
        key_name                                          = input("Enter keyname : ")
        target_file                                       = input("Enter File name (Full path) : ")
        secure_obj.decrypt(key_name,target_file)
try                                                       : 
    main()
except                                                    : 
    print("[-] ERROR")