from cryptography.fernet import Fernet
import hashlib
import base64


def genkey(key):
        hashedKey = hashlib.sha256(key.encode()).digest()
        kodKey = base64.urlsafe_b64encode(hashedKey)

        while len(kodKey) < 32:
            kodKey += b'='
        return kodKey

def encrypt( key, path):
        fernet = Fernet(key)
        with open(path, "rb") as f:
            fb = f.read()
        encrptbytes = fernet.encrypt(fb)
        with open(path, "wb") as f:
            f.write(encrptbytes)

def decrypt(key, path):
        fernet = Fernet(key)
        with open(path, "rb") as f:
            fb = f.read()
        encrptbytes = fernet.decrypt(fb)
        with open(path, "wb") as f:
            f.write(encrptbytes)