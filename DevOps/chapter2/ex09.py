import hashlib

secret = "Objects are passed into a template from the template engine"
print(secret)

bsecret = secret.encode()
print(bsecret)

m = hashlib.md5()
print(m)

m.update(bsecret)
print(bsecret)

m.digest()
print(m)