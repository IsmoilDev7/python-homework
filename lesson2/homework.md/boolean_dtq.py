#1. Write a program that accepts a username and password and checks if both are not empty.

username = input("enter username: ")
password = input("enter password: ")

isempty = bool(username.strip()) and bool(password.strip())

print("Both are not empty: ", isempty)

#2. Create a program that checks if two numbers are equal and outputs a message if they are.

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

print("They are equal: " * (num1 == num2))

#3. Write a program that checks if a number is positive and even.

number1 = int(input("enter number: "))

result = bool(number1 > 0 and number1 % 2 == 0)

print("Is number positive and even: ", result)
