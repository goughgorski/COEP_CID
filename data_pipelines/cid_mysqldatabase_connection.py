
from cryptography.fernet import Fernet
import configparser

with open('config.ini', 'r') as config_file:
    config = configparser.ConfigParser()
    config.read_file(config_file)
    encrypted_string = config.get('DEFAULT', 'mysql_password')
    
with open('cipher.ini', 'r') as cipher_file:
    cipher = configparser.ConfigParser()
    cipher.read_file(cipher_file)
    cipher_string = cipher.get('DEFAULT', 'cipher_string')

cipher_suite = Fernet(cipher_string)
decrypted_bytes = cipher_suite.decrypt(encrypted_string.encode())

decrypted_connection_string = decrypted_bytes.decode()

class MySQL:
    def return_mysql_password():
        return(decrypted_connection_string)
