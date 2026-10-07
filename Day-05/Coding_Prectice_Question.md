```python
# Python 90 Days Challenge
# Day 05 - Strings Practice Questions & Solutions

# Python 90 Days Challenge
# Day 05 - Strings Practice


# ==========================================
# PRACTICE QUESTIONS
# ==========================================

# Q1. Write a Python program to reverse a given string.

# Q2. Write a Python program to check whether a given string
#     is a palindrome or not.

# Q3. Write a Python program to count the number of vowels
#     and consonants in a given string.

# Q4. Write a Python program to count the number of characters
#     in a string without using len().

# Q5. Write a Python program to count the frequency of a
#     given character in a string.

# Q6. Write a Python program to remove all spaces from a string.

# Q7. Write a Python program to find duplicate characters
#     in a given string.

# Q8. Write a Python program to check whether two strings
#     are anagrams or not.

# Q9. Write a Python program to find the first non-repeating
#     character in a string.

# Q10. Write a Python program to count vowels, consonants,
#      digits, and special characters in a given string.


# ==========================================
# PRACTICE INSTRUCTION
# ==========================================

# First, try to solve all the questions yourself.
# Do not look at the solution immediately.
# If you cannot solve a question, revise the String topic
# and understand the logic before moving forward.


# ==================================================
# Q1. Reverse a String
# ==================================================

text = input("Enter a string: ")

print("Reversed String:", text[::-1])


# ==================================================
# Q2. Check Palindrome String
# ==================================================

text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# ==================================================
# Q3. Count Vowels and Consonants
# ==================================================

text = input("Enter a string: ")

vowels = 0
consonants = 0

for char in text:

    if char.lower() in "aeiou":
        vowels += 1

    elif char.isalpha():
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)


# ==================================================
# Q4. Count Characters Without Using len()
# ==================================================

text = input("Enter a string: ")

count = 0

for char in text:
    count += 1

print("Number of characters:", count)


# ==================================================
# Q5. Count Frequency of a Character
# ==================================================

text = input("Enter a string: ")
character = input("Enter a character: ")

count = 0

for char in text:

    if char == character:
        count += 1

print("Frequency:", count)


# ==================================================
# Q6. Remove Spaces from a String
# ==================================================

text = input("Enter a string: ")

result = text.replace(" ", "")

print("String without spaces:", result)


# ==================================================
# Q7. Find Duplicate Characters
# ==================================================

text = input("Enter a string: ")

duplicates = ""

for char in text:

    if text.count(char) > 1 and char not in duplicates:
        duplicates += char

print("Duplicate characters:", duplicates)


# ==================================================
# Q8. Check Anagram Strings
# ==================================================

text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

if sorted(text1) == sorted(text2):
    print("Anagram")
else:
    print("Not Anagram")


# ==================================================
# Q9. Find First Non-Repeating Character
# ==================================================

text = input("Enter a string: ")

for char in text:

    if text.count(char) == 1:
        print("First non-repeating character:", char)
        break

else:
    print("No non-repeating character found")


# ==================================================
# Q10. Count Vowels, Consonants, Digits and
#      Special Characters
# ==================================================

text = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
special = 0

for char in text:

    if char.lower() in "aeiou":
        vowels += 1

    elif char.isalpha():
        consonants += 1

    elif char.isdigit():
        digits += 1

    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special Characters:", special)
```
