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

#6. Write a Python program to check if one string contains another.

txt5 = input("enter txt: ")
word = input("enter word: ")

print("Contains: ", word in txt5)

#7. Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.
#Example:

#Input sentence: "I love apples."
#Replace: "apples"
#With: "oranges"
#Output: "I love oranges."

sentence = input("enter sentence: ")
word_to_replace = input("enter word to replace: ")
replacement_word = input("enter replacement word: ")

new_sentence = sentence.replace(word_to_replace, replacement_word)

print("New sentence: ", new_sentence)

#8. Write a program that asks the user for a string and prints the first and last characters of the string.

txt6 = input("enter txt: ")

print(f"first word: {txt6[0]}\nLast word: {txt6[-1]}")

#9. Ask the user for a string and print the reversed version of it.

txt7 = input("enter txt: ")
print("Reversed: ", txt7[::-1])

#10. Write a program that asks the user for a sentence and prints the number of words in it.

txt8 = input("enter sentence: ")

words1 = txt8.split()

print("Number of words: ", len(words1))

#11. Write a program to check if a string contains any digits.

txt9 = input("enter txt: ")

isword = not txt9.isalpha() and not not txt9.isspace() and not txt9 != ""

print("Contains digit: ", isword)

#12. Write a program that takes a list of words and joins them into a single string, separated by a character (e.g., - or ,).

lists = ["Kundan", "kun"]

joined_string = "-".join(lists)

print("Joined string: ", joined_string)

#13. Ask the user for a string and remove all spaces from it.

txt10 = input("enter txt: ")

print("Remove spaces: ", txt10.replace(" ", ""))

#14. Write a program to ask for two strings and check if they are equal or not.

txt_1 = input("enter first txt: ")
txt_2 = inout("enter second txt: ")

print("Is equel: ", txt_1 == txt_2)

#15. Ask the user for a sentence and create an acronym from the first letters of each word.
#Example:

#Input: "World Health Organization"
#Output: "WHO"

#16. 