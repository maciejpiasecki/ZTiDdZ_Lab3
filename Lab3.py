#Zad 1

import base64

def string_to_base64(string):

    # Encode the input string into bytes using ASCII
    string_bytes = string.encode("ascii")

    # Use base64 encoding to convert the string bytes into base64
    base64_bytes = base64.b64encode(string_bytes)

    # Decode the base64 bytes back into a base64 string using ASCII
    base64_string = base64_bytes.decode("ascii")
    return base64_string

print(string_to_base64("Lab 3"))

#Zad 2

import random
import string

def password_generator():
    
    # Base for password creation
    char =  string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    pwd_length = random.randint(8,32)
    
    # Password generation
    while True:
        pwd = "".join(random.choice(char) for _ in range(pwd_length))
        
        # Checking if the password meets all the conditions
        if all([
            len(pwd) >= 8,
            any(c in string.ascii_lowercase for c in pwd),
            any(c in string.ascii_uppercase for c in pwd),
            any(c in string.digits for c in pwd),
            any(c in string.punctuation for c in pwd)
        ]):
            return pwd

print(password_generator())

