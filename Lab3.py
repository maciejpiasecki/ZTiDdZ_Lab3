#Zad 1

import base64
def string_to_base641(string):
    string_bytes = string.encode("ascii")
    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string

#Zad 2

import random
import string


def password_generator():
    char =  string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    pwd_length = random.randint(8,32)

    while True:
        pwd = "".join(random.choice(char) for _ in range(pwd_length))

        if all([
            any(c in string.ascii_lowercase for c in pwd),
            any(c in string.ascii_uppercase for c in pwd),
            any(c in string.digits for c in pwd),
            any(c in string.punctuation for c in pwd)
        ]):
            return pwd

