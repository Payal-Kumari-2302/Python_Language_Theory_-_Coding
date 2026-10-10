# Python 90 Days Challenge
# Day 08 - Loops and Iteration
# Coding Practice Questions

# ==============================
# QUESTIONS
# ==============================

# Q1. Print numbers from 1 to 5 using a for loop.

# Q2. Print each character of the string "Python"
#     using a for loop.

# Q3. Print numbers from 1 to 10 using range().

# Q4. Print numbers from 5 to 1 using a for loop.

# Q5. Print numbers from 1 to 5 using a while loop.

# Q6. Print numbers from 1 to 10 using a while loop.

# Q7. Print even numbers from 2 to 10 using a for loop.

# Q8. Calculate the sum of numbers from 1 to 10
#     using a for loop.

# Q9. Calculate the sum of numbers from 1 to 10
#     using a while loop.

# Q10. Display the multiplication table of a number
#      using a for loop.

# Q11. Count the characters in the string "Programming"
#      using a for loop.

# Q12. Print all elements of a list one by one
#      using a for loop.

# Q13. Print numbers from 1 to 10 using a while loop.

# Q14. Ask the user to enter a password repeatedly
#      until the correct password is entered.

# Q15. Print numbers from 1 to 5 using both for and
#      while loops.


# ==============================
# INSTRUCTIONS
# ==============================

# 1. Read each question carefully.
# 2. Try to solve the questions before checking solutions.
# 3. Understand the use of for and while loops.
# 4. Use proper indentation.
# 5. Run each program and verify its output.
# 6. Save your practice in the Day-08 folder.


# ==============================
# SOLUTIONS
# ==============================

# Q1. Print numbers from 1 to 5 using a for loop.

for number in range(1, 6):
    print(number)


# Q2. Print each character of "Python".

word = "Python"

for letter in word:
    print(letter)


# Q3. Print numbers from 1 to 10 using range().

for number in range(1, 11):
    print(number)


# Q4. Print numbers from 5 to 1.

for number in range(5, 0, -1):
    print(number)


# Q5. Print numbers from 1 to 5 using a while loop.

number = 1

while number <= 5:
    print(number)
    number += 1


# Q6. Print numbers from 1 to 10 using a while loop.

number = 1

while number <= 10:
    print(number)
    number += 1


# Q7. Print even numbers from 2 to 10.

for number in range(2, 11, 2):
    print(number)


# Q8. Calculate the sum from 1 to 10 using a for loop.

total = 0

for number in range(1, 11):
    total += number

print("Sum:", total)


# Q9. Calculate the sum from 1 to 10 using a while loop.

number = 1
total = 0

while number <= 10:
    total += number
    number += 1

print("Sum:", total)


# Q10. Display the multiplication table of a number.

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# Q11. Count characters in "Programming" using a for loop.

word = "Programming"
count = 0

for character in word:
    count += 1

print("Total characters:", count)


# Q12. Print all elements of a list.

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)


# Q13. Print numbers from 1 to 10 using a while loop.

number = 1

while number <= 10:
    print(number)
    number += 1


# Q14. Repeat password input until the correct password.

correct_password = "python123"
password = ""

while password != correct_password:
    password = input("Enter password: ")

print("Access granted!")


# Q15. Print numbers from 1 to 5 using both loops.

print("Using for loop:")

for number in range(1, 6):
    print(number)

print("Using while loop:")

number = 1

while number <= 5:
    print(number)
    number += 1
