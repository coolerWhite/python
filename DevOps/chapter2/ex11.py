from cryptography.hazmat.backends import default_backend

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa,padding

privat_key = rsa.generate_private_key(public_exponent=65537, key_size=4096, backend=default_backend())
print(privat_key)

public_key = privat_key.public_key()
print(public_key)

message = b"New Secret Message for ME!"
# шифровка
enc = public_key.encrypt(message, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
print(enc)
# рассшифровка
dec = privat_key.decrypt(enc, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
print(dec)