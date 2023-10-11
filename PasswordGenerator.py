import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

passwordLength = int(input("Enter the desired length of the password: "))

password = ""
for i in range(passwordLength):
    password += random.choice(characters)

print("Your password is:", password)