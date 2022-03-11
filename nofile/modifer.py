import base64
from cryptography.fernet import Fernet, InvalidToken
from . import io
from .key import Key

def add(title:str, data:str, key:Key):
    message = title+":"+data
    io.append(key.encrypt(message))

def get(title:str, key:Key):
    for k in io.getList():
        try:
            f = key.decrypt(k)
        except InvalidToken:
            raise ValueError("Incorrect Key, corrupted file or incorrect search!")
        if f[0] == title:
            return f

def getKey(key:str) -> Key:
    if len(key)>32:
        raise ValueError("error: key cant be longer than 32 characters!")
    elif len(key)==32:
        return Key(key)
    elif key==None: # if the key isnt provided
        k = input("Enter key: ")
        return Key(k)
    else:
        return Key(key+"0"*(32-len(key)))