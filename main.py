import random
import string
length=int(input("enter length of password"))
list= string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(length):
    password+=(random.choice(list))
print(f"Your password is {password}")
