import pyAesCrypt

def crypter(_mode, _file):
    password = input("Enter password: ")
    buffer = 512 * 1024
    ext = _file.split(".")
    if(int(_mode) == 0):
        pyAesCrypt.encryptFile(_file, ext[0].lower() + ".br", password, buffer)
    elif(int(_mode) == 1):
        _type = input("Enter Type: ")
        pyAesCrypt.decryptFile(_file, ext[0].lower() + "." + _type, password,buffer)

print("--- BR Crypter ---")
print("0 - Crypt")
print("1 - Decrypt")

mode = input("Enter mode: ")
filename = input("Enter file name: ")
crypter(mode, filename)