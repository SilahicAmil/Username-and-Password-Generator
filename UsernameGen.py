import string
from random import *

usernamechar = string.ascii_uppercase + string.digits

username = "".join(choice(usernamechar) for x in range(7))

print(username)

