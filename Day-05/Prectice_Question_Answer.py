```python
# Python 90 Days Challenge
# Day 05 - Strings Practice


# ==========================================
# String Creation
# ==========================================

s1 = "Hello"
s2 = "Python"


# Take your first name and last name as input and print your full name.

first_name = "Payal"
last_name = "Kumari"

full_name = first_name + " " + last_name

print(full_name)


# Take a string as input and print the first character.

s = "Payal"

print(s[0])


# Take a string as input and print the last character.

print(s[4])


# Take a string as input and print the first and last character.

print(s[0])
print(s[4])


# Take a string as input and print each character one by one.

print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# print(s[5])  # This will show an IndexError.


# Take a string as input and count the number of
# vowels, consonants, digits, and special characters.

x = "Payal"

v = 0
c = 0
d = 0
sc = 0

for i in x:

    if i.lower() in "aeiou":
        v = v + 1

    elif i.isalpha():
        c = c + 1

    elif i.isdigit():
        d = d + 1

    else:
        sc = sc + 1

print("Vowel:", v)
print("Consonant:", c)
print("Digit:", d)
print("Special Character:", sc)


# ==========================================
# Concatenation (+)
# ==========================================

# Take two strings as input and join them using +.

s1 = "Payal"
s2 = "Kumari"

s = s1 + " " + s2

print(s)


# Take first name and last name and create the full name using +.

first_name = "Payal"
last_name = "Kumari"

full_name = first_name + " " + last_name

print(full_name)


# ==========================================
# Repetition (*)
# ==========================================

# Take a string and a number as input,
# then print the string that many times.

name = "Payal"

result = name * 3

print(result)


# Print "Python" 3 times using *.

print("Python" * 3)


# ==========================================
# Indexing
# ==========================================

# Take a string and print its first,
# second and third characters using indexing.

s = "Payal"

print(s[0])
print(s[1])
print(s[2])


# Take a string and print the first and last character using indexing.

print(s[0])
print(s[4])


# ==========================================
# String Slicing
# ==========================================

# Take a string and print its first 3 characters using slicing.

s = "Payal"

print(s[0:3])


# Take a string and print the last 3 characters using slicing.

print(s[-3:])


# Extra

word = "Python"

print(word[0:3])       # Pyt
print(word[2:])        # thon
print(word[:4])        # Pyth


# You can also use step values.

print(word[0:6:2])     # Pto

print(word[::-1])      # nohtyP (Reverse)


# ==========================================
# Membership (in / not in)
# ==========================================

# Take a string and a character as input.
# Check whether the character is present using in.

s = "Payal"

print("P" in s)


# Take a string and a character as input.
# Check whether the character is not present using not in.

print("K" not in s)


# Extra

s = "Hello World"

print("world" in s)        # False
print("Python" not in s)   # True
print("Print" in s)        # False
print("Hello" in s)        # True


# ==========================================
# All String Methods
# ==========================================


# ==========================================
# 1. Case Conversion
# ==========================================

name = "Payal"

# Length()
print(len(name))


# Upper() case
print(name.upper())


# Lower() case
print(name.lower())


# Capitalize()
name = "payal"

print(name.capitalize())


# Title()
name = "mahi"

print(name.title())


# Swapcase()
print(name.swapcase())


# CaseFold()
name = "PAYAL"

print(name.casefold())


# ==========================================
# 2. Searching / Finding
# ==========================================

# find()
name = "Payal"

print(name.find("y"))


# rfind()
# rfind() means searching from the right side
# and finding the last occurrence.

name = "Payal"

print(name.rfind("a"))


# index()
name = "Payal"

print(name.index("P"))


# rindex()
name = "Payal"

print(name.rindex("y"))


# count()
name = "Payal"

print(name.count("l"))


# startswith()
name = "Payal"

print(name.startswith("Pa"))


# endswith()
print(name.endswith("l"))


# ==========================================
# 3. Checking String Content
# ==========================================

# isalpha()
name = "Payal"

print(name.isalpha())


# isdigit()
num = "123"

print(num.isdigit())


# isdecimal()
num = "123"

print(num.isdecimal())


# isnumeric()
num = "123"

print(num.isnumeric())


# isalnum()
print("Payal2302".isalnum())


# isspace()
print(" ".isspace())


# islower()
print("payal".islower())


# isupper()
print("HELLO".isupper())


# istitle()
print("Hello World".istitle())


# isidentifier()
print("name".isidentifier())


# isascii()
print("Hello".isascii())


# isprintable()
print("Hello".isprintable())


# ==========================================
# 4. Replace / Split / Join
# ==========================================

# replace()
print("Hello".replace("H", "Y"))


# split()
print("a b c".split())


# rsplit()
print("a-b-c".rsplit("-", 1))


# splitlines()
print("a\nb".splitlines())


# join()
print("-".join(["a", "b"]))


# partition()
print("a-b".partition("-"))


# rpartition()
print("a-b-c".rpartition("-"))


# ==========================================
# 5. Removing / Cleaning Methods
# ==========================================

# strip()
print(" Hello ".strip())


# lstrip()
print(" Hello".lstrip())


# rstrip()
print("Hello ".rstrip())


# removeprefi
```
