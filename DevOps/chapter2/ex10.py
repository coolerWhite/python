from cryptography.fernet import Fernet
# создание ключа
key = Fernet.generate_key()

print(key)
# шифровка сообщения
f = Fernet(key)

message = b"Secter Message for ME"

encrypt = f.encrypt(message)

print(encrypt)

# рассшифровка

p = Fernet(key)
print(p.decrypt(encrypt))