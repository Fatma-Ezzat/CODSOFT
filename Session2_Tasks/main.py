# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Task1: Write a program to enter a number from a user and print its absolute value.
num = float(input("Enter your number: "))
print("Absolute Value is: ", abs(num))
 # Another Solution
num = float(input("Enter your number: "))
if num < 0:
    print("Absolute Value is: ", num * (-1))
else:
    print("Absolute Value is: ", num)

# Task2: Write a program to enter a year from a user and check if it is a leap year or not.
year = int(input("Enter your desired year: "))
if year % 4 == 0:
    print("THIS IS A LEAP YEAR:)")
else:
    print("THIS IS NOT A LEAP YEAR:)")

# Task3: Write a program to enter the age of 3 person and print the oldest and the youngest among them
i = 1
age1 = float(input("Enter the age of the first person: "))
age2 = float(input("Enter the age of the second person: "))
age3 = float(input("Enter the age of the third person: "))
if age1 > age2 and age1 > age3:
    print("First person is the oldest person")
if age1 < age2 and age1 < age3:
    print("First person is the youngest person")
if age2 > age1 and age2 > age3:
    print("Second person is the oldest one")
if age2 < age1 and age2 < age3:
    print("Second person is the youngest one")
if age3 > age1 and age3 > age2:
    print("Third person is the oldest one")
if age3 < age1 and age3 < age2:
    print("Third person is the youngest one")
if age1 == age2 and age2 > age3:
    print("First and Second person are the oldest ones")
if age1 == age3 and age3 > age2:
    print("First and Third person are the oldest ones")
if age2 == age3 and age3 > age1:
    print("Second and Third person are the oldest ones")
if age1 == age2 and age2 < age3:
    print("First and Second person are the youngest ones")
if age1 == age3 and age3 < age2:
    print("First and Third person are the youngest ones")
if age2 == age3 and age3 < age1:
    print("Second and Third person are the youngest ones")

# Task4: What is the name of the library that encrypted the number like the password?
    # We can use getpass module
import getpass
password = getpass.getpass("Enter your password: ")
print("Your Password is: ", password)


