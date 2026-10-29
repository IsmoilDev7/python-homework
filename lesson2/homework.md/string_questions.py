#1. Create a program to ask name and year of birth from user and tell them their age.

name = input("enter name: ")
birth_year = input("enter birth year: ")

age = 2026 - int(birth_year)

print(f"{name} your age is {age}")

#2. Extract car names from this text: txt = 'LMaasleitbtui'

txt = 'LMaasleitbtui'

print("Car names: ", txt[::2], txt[1::2])

#3. Write a Python program to:

#Take a string input from the user.
#Print the length of the string.
#onvert the string to uppercase and lowercase.

txts = input("enter txt: ")

print("Leng: ", len(txts))
print("Upper: ", txts.upper())
print("Lower: ", txts.lower())

#4. Write a Python program to check if a given string is palindrome or not.
#What is a Palindrome String? A string is called a palindrome if the reverse of the string is the same as the original one. Example: “madam”, “racecar”, “12321”.

txt3 = input("enter txt: ")

print("Is palin: ", txt3 == txt3[::-1]) #[::-1] is used to reverse the string

#5. Write a program that counts the number of vowels and consonants in a given string.

txt4 = input("enter txt: ").lower()

vowels = (txt4.count("a") + txt4.count("e") + 
          txt4.count("i") + txt4.count("o") + 
          txt4.count("u"))

letters = txt4.replace(" ", "")
cons = len(letters) - vowels

print(f"Vowels: {vowels}\nConsonants: {cons}")


