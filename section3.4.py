import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def get_hash(message):
    return hashlib.sha256(message.encode()).hexdigest()

def symmetric_encryption():
    key = Fernet.generate_key()
    cipher = Fernet(key)
    original_text = "Конфіденційна інформація"
    
    encrypted = cipher.encrypt(original_text.encode())
    decrypted = cipher.decrypt(encrypted).decode()
    return encrypted, decrypted

def rsa_signature():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    
    message = b"Signed by Student"
    signature = private_key.sign(
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    return signature

msg = "Hello Python"
print(f"Повідомлення: {msg}")
print(f"SHA-256 Геш: {get_hash(msg)}")

enc, dec = symmetric_encryption()
print(f"\nAES Зашифровано: {enc}")
print(f"AES Розшифровано: {dec}")

sig = rsa_signature()
print(f"\nRSA Цифровий підпис створено: {sig.hex()[:50]}...")