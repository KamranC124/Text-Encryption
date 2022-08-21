from cryptography.fernet import Fernet

def GenerateKey():
    Key = Fernet.generate_key()
    KeyFile = open("Key.key", "wb")
    KeyFile.write(Key)
    KeyFile.close()
    print("Key created.")
    
while 1:
    try:
        with open('Key.key', 'rb') as UserKey:
            Key = UserKey.read()
            print("Key found.")
            break
    except FileNotFoundError:
        print("Key not found.")
        GenerateKey()
        
f = Fernet(Key)

def EncryptFile(ChosenFile):
    with open(ChosenFile, 'rb') as OriginalFile:
        Original = OriginalFile.read()
    Encrypted = f.encrypt(Original)
    with open (ChosenFile, 'wb') as EncryptedFile:
        EncryptedFile.write(Encrypted)
    print("File encrypyed.")

def DecryptFile(ChosenFile):
    with open (ChosenFile, 'rb') as EncryptedFile:
        Encrypted = EncryptedFile.read()
    Decrypted = f.decrypt(Encrypted)
    with open(ChosenFile, 'wb') as DecryptedFile:
        DecryptedFile.write(Decrypted)
    print("File decrypted.")

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
