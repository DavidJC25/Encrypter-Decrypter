import os
from genericpath import exists
from cryptography.fernet import Fernet
from pathlib import Path

def encrypt(path):
    for file in os.scandir(path):

        if os.path.isdir(file):
            encrypt(file.path)
        else:
            with open(file, "rb") as openedFile:
                content = openedFile.read()
            encContent = Fernet(key).encrypt(content)

            with open(file, "wb") as openedFile:
                openedFile.write(encContent)

keyFolderPath = Path(__file__).parent / "Key"
if not os.path.exists(keyFolderPath):
    os.mkdir(Path(__file__).parent / "Key")

keyPath = Path(__file__).parent / "Key/secretKey.key"
if not os.path.exists(keyPath):
    key = Fernet.generate_key()
    with open(keyPath, "wb") as secretKey:
        secretKey.write(key)
else:
    with open(keyPath, "rb") as secretKey:
        key=secretKey.read()

path = Path(__file__).parent / "Files"

encrypt(path)



