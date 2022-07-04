import os
from cryptography.fernet import Fernet
from pathlib import Path

def decrypt(path):
    for file in os.scandir(path):
        
        if os.path.isdir(file):
            decrypt(file.path)
        else:
            with open(file, "rb") as openedFile:
                encContent = openedFile.read()
            content = Fernet(key).decrypt(encContent)

            with open(file, "wb") as openedFile:
                openedFile.write(content)


keyFolderPath = Path(__file__).parent / "Key"
if not os.path.exists(keyFolderPath):
    os.mkdir(Path(__file__).parent / "Key")

keyPath = Path(__file__).parent / "Key/secretKey.key"

if not os.path.exists(keyPath):
    raise Exception("Key Not Found.")

with open(keyPath, "rb") as secretKey:
    key=secretKey.read()

path = Path(__file__).parent / "Files"

decrypt(path)

