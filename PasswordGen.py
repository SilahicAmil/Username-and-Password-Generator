import string
from random import *

characters = string.ascii_letters + string.digits + string.ascii_uppercase + string.punctuation

password = "".join(choice(characters) for x in range (randint(10,16)))

print(password)