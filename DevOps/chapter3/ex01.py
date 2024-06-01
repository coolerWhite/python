import sys
# порядок байтов в архитектуре
print(sys.byteorder) 

# размер объектов Python
print(sys.getsizeof(1))

# архитектура
print(sys.platform)

# узнать версию python
print(sys.version_info)

if sys.version_info.major > 2:
    print("python version > 2")
elif sys.version_info.micro > 9:
    print("python version 3.x > 9")
else:
    pass