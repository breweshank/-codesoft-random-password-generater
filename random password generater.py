import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbol = " !@#$%*&"

all_char = lower + upper + numbers + symbol
length = int(input("Enter the length of the password: "))

password = ''.join(random.sample(all_char, length))
print("Genearted Password: ", password)
C:\Users\ESHANK\AppData\Roaming\JetBrains\PyCharm2024.1\scratches\random password generater.py