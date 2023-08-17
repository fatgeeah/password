import os 
import base64 
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

# password = b'password'

# salt random letter
# salt = os.urandom(16)
# print(salt)

# Password Based Key Derivation
# kdf = PBKDF2HMAC (
#     algorithm=hashes.SHA256(),
#     length=32,
#     salt=salt,
#     iterations=100000,
#     backend=default_backend()
# )

# key = kdf.derive(password)

# kdf.verify(password,key)

# key = base64.urlsafe_b64decode(kdf.derive(b'passwordpassword'))
# f = Fernet(key)

