
import uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from cryptography.fernet import Fernet
import configparser

with open('config.ini', 'r') as config_file:
    config = configparser.ConfigParser()
    config.read_file(config_file)
    encrypted_string = config.get('DEFAULT', 'container_connection_string')
    
with open('cipher.ini', 'r') as cipher_file:
    cipher = configparser.ConfigParser()
    cipher.read_file(cipher_file)
    cipher_string = cipher.get('DEFAULT', 'cipher_string')
    
cipher_suite = Fernet(cipher_string)
decrypted_bytes = cipher_suite.decrypt(encrypted_string.encode())

decrypted_connection_string = decrypted_bytes.decode()

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(decrypted_connection_string)

# Access a specific container within the storage account
container_name = "coepcid"
container_client = blob_service_client.get_container_client(container_name)

class Container:
    def __init__():
        
        connection.blob_service_client = blob_service_client
        connection.container_client = container_client
              
    def return_container_client():
        return(container_client)
    
    def return_blob_service_client():
        return(blob_service_client)
    
    def return_container_name():
        return(container_name)
        
