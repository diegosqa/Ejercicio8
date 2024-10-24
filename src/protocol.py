from cryptography.fernet import Fernet

class Protocol:
    def __init__(self, token):
        self.token = token
        self.encryption_key = Fernet.generate_key()
        self.cipher = Fernet(self.encryption_key)
        self.authenticated = False
    
    def authenticate(self, token_provided):
        if token_provided == self.token:
            self.authenticated = True
        else:
            raise ValueError("Error: Autenticación fallida")
    
    def send_message(self, message):
        if not self.authenticated:
            raise ValueError("Error: Usuario no autenticado")
        encrypted_message = self.cipher.encrypt(message.encode())
        return encrypted_message

    def receive_message(self, encrypted_message):
        if not self.authenticated:
            raise ValueError("Error: Usuario no autenticado")
        decrypted_message = self.cipher.decrypt(encrypted_message).decode()
        return decrypted_message

