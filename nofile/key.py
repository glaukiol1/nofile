from cryptography.fernet import Fernet
import base64

class Key:
    def __init__(self, password:str):
        self.password = password
        self.fernet = Fernet(base64.encodebytes(self.password.encode('utf-8')))
    
    def encrypt(self, data:str) -> str:
        return self.fernet.encrypt(data.encode()).decode('utf-8')+';'

    def decrypt(self, hash:str) -> list:
        return (
            self.fernet.decrypt(bytes(hash, "utf-8")).decode('utf-8').replace(";","").split(":")
        )