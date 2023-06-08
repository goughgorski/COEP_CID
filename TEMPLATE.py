
## 1. WRITE CONNECTION SCRIPT AS .py FILE

#%%writefile connection_example.py

## 1. IMPORT CRYPTOGRAPHY AND CONFIG PACKAGES (AND ANY OTHER NECESSARY PACKAGES)

#from cryptography.fernet import Fernet
#import configparser

## 2. OPEN LOCAL CONFIG FILE (**NOTE: CONFIG FILE MUST BE CREATED AND SAVED IN LOCAL DIRECTORY)

#with open('config.ini', 'r') as config_file:
#    config = configparser.ConfigParser()
#    config.read_file(config_file)
#    encrypted_string = config.get('DEFAULT', 'connection_string')
    
## 3. OPEN CIPHER FILE
    
#with open('cipher.ini', 'r') as cipher_file:

#    cipher = configparser.ConfigParser()
#    cipher.read_file(cipher_file)
#    cipher_string = cipher.get('DEFAULT', 'cipher_string')
    
## 4. USE CIPHER TO DECRYPT CONNECTION INFORMATION 
    
#cipher_suite = Fernet(cipher_string)
#decrypted_bytes = cipher_suite.decrypt(encrypted_string.encode())

#decrypted_connection_string = decrypted_bytes.decode()

## 5. CREATE CONNECTION CLASS WITH INDIVIDUAL FUNCTION FOR EACH PIECE OF INFORMATION
#class Connection:

#    def return_connection_password():
#        return(decrypted_connection_string)
    
## 6. ACCESS CONNECTION INFORMATION IN A NEW NOTEBOOK BY IMPORTING THE CONNECTION CLASS CREATED

#from connection_example import Connection as c

#password = c.return_connection_password()
