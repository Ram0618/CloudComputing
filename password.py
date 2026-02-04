import random
import string

length = 8
password = ""

for _ in range(length):
    password += random.choice(string.ascii_letters + string.digits)

print(password)
