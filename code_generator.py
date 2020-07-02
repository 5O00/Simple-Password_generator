import random, string

characters = string.printable
password = ""
password_size = int(input("Enter the size of you're password : "))

for i in range(password_size):
    num = random.randint(0, 99)
    password = password + characters[num]

print(password)