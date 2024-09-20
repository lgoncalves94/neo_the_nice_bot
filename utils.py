from cryptograhoy.fernet import Fernet

def encrypt_data(user_key, data):
    cipher = Fernet(user_key)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data

def decrypt_data(user_key, encrypted_data):
    cipher = Fernet(user_key)
    decrypted_data = cipher.decrypt(encrypted_data).decode()
    return decrypted_data