from cryptography.fernet import Fernet

def GenerateKey():
    Key = Fernet.generate_key()
    KeyFile = open("Key.key", "wb")
    KeyFile.write(Key)
    KeyFile.close()
    print("Key created.")
    
while 1:
    try:
        with open('Key.key', 'rb') as MyKey:
            Key = MyKey.read()
            print("Key found.")
            break
    except FileNotFoundError:
        print("Key not found.")
        GenerateKey()
        
f = Fernet(Key)

def EncryptFile(ChosenFile):
    with open(ChosenFile, 'rb') as OriginalFile:
        original = OriginalFile.read()
    encrypted = f.encrypt(original)
    with open (ChosenFile, 'wb') as EncryptedFile:
        EncryptedFile.write(encrypted)
    print("File encrypyed.")

def DecryptFile(ChosenFile):
    with open (ChosenFile, 'rb') as EncryptedFile:
        encrypted = EncryptedFile.read()
    decrypted = f.decrypt(encrypted)
    with open(ChosenFile, 'wb') as DecryptedFile:
        DecryptedFile.write(decrypted)
    print("File decrypyed.")

ChosenFile = input("Enter file path: ")
MenuOption = int(input("\nChoose one: \n1. Encrypt \n2. Decrypt \n"))

try:
    if MenuOption == 1:
        EncryptFile(ChosenFile)
    elif MenuOption == 2:
        DecryptFile(ChosenFile)
    else:
        raise
except:
    print("Error. Check file location, or menu option.")
