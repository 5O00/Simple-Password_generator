import random, string

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password = ""
password_size = int(input("Enter the size of you're password : "))

for i in range(password_size):
    num = random.randint(0, len(characters)-1)
    password = password + characters[num]

print(password)
