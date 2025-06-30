import hashlib

def hash(text):
    hashed = hashlib.md5(text.encode()).hexdigest()
    return hashed