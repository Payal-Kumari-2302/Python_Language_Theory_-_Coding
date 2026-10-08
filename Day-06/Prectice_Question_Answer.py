```python
# Python 90 Days Challenge
# Day 06 - Control Flow Practice Questions & Solutions


# ==========================================
# PRACTICE QUESTIONS
# ==========================================

# Q1. Take a number as input and check whether the number
#     is positive.

# Q2. Take a number as input and check whether the number
#     is positive, negative, or zero.

# Q3. Take a number as input and check whether it is
#     even or odd.

# Q4. Take two numbers as input and print the greater number.

# Q5. Take two numbers as input and check whether they
#     are equal or which one is greater.

# Q6. Take a person's age as input and check whether the
#     person is eligible to vote.

# Q7. Take marks as input and check whether the student
#     has passed or failed.
#     Passing marks = 40

# Q8. Take marks as input and display the grade:
#     90 or above → Grade A
#     75 or above → Grade B
#     40 or above → Grade C
#     Below 40 → Fail

# Q9. Take three numbers as input and find the largest number.

# Q10. Take a number as input and check whether it is
#      divisible by both 5 and 10.


# ==========================================
# PRACTICE INSTRUCTION
# ==========================================

# First, try to solve all the questions yourself.
# Do not look at the solution immediately.
# If you cannot solve a question, revise the if,
# if-else and elif concepts and understand the logic
# before moving forward.


# ==================================================
# Q1. Check Positive Number
# ==================================================

number = int(input("Enter a number: "))

if number > 0:
    print("Positive")


# ==================================================
# Q2. Positive, Negative or Zero
# ==================================================

number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# ==================================================
# Q3. Check Even or Odd
# ==================================================

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# ==================================================
# Q4. Find Greater Number
# ==================================================

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Greater number:", a)
else:
    print("Greater number:", b)


# ==================================================
# Q5. Compare Two Numbers
# ==================================================

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is greater")
elif b > a:
    print("Second number is greater")
else:
    print("Both numbers are equal")


# ==================================================
# Q6. Voting Eligibility
# ==================================================

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# ==================================================
# Q7. Pass or Fail
# ==================================================

marks = int(input("Enter your marks: "))

if marks >= 40:
    print("Passed")
else:
    print("Failed")


# ==================================================
# Q8. Grade System
# ==================================================

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")


# ==================================================
# Q9. Find Largest of Three Numbers
# ==================================================

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)


# ==================================================
# Q10. Divisible by 5 and 10
# ==================================================

number = int(input("Enter a number: "))

if number % 5 == 0 and number % 10 == 0:
    print("Number is divisible by both 5 and 10")
else:
    print("Number is not divisible by both 5 and 10")
```
