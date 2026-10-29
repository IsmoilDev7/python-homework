import math
#1. Create a program that takes a float number as input and rounds it to 2 decimal places.

son = float(input("Enter float number: "))

print(f"{son:.2f}")

#Write a Python file that asks for three numbers and outputs the largest and smallest.

a = float(input("enter first number: "))
b = float(input("enter second number: "))
c = float(input("enter third number: "))

print("Max number: ", max(a, b, c))
print("Min number: ", min(a, b, c))

#3. Create a program that converts kilometers to meters and centimeters.

km = float(input("enter kilometer: "))

metr = km*1000
santr = km*100000

print(f"{metr} meters\n{santr} centimeters")

#4. Write a program that takes two numbers and prints out the result of integer division and theremainder.

aa = int(input("enter first num: "))
bb = int(input("enter second num: "))

print(f"Integer division: {aa // bb}\nRemainder: {aa % bb}")

#5. Make a program that converts a given Celsius temperature to Fahrenheit.

celsius = float(input("enter celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")

#6. Create a program that accepts a number and returns the last digit of that number.

number = int(input("enter num: "))

last_digit = abs(number) % 10

print(f"Last digit {number}")

#7. Create a program that takes a number and checks if it’s even or not.

even_or_not = int(input("enter num: "))

print("even or not: ", even_or_not % 2 == 0)
