```python
# Python 90 Days Challenge
# Day 07 - Practice Questions & Solutions

# Topics:
# 1. Nested Conditions
# 2. Ternary Operator
# 3. match-case
# 4. Truthy and Falsy Values


# ==================================================
# PART 1: PRACTICE QUESTIONS
# ==================================================

# Q1. Write a program to check voting eligibility based on age.

# Q2. Write a program to check whether a number is positive, negative, or zero.

# Q3. Write a program to determine whether a person is an adult or a minor
#     using the ternary operator.

# Q4. Write a program to check whether a string is empty or non-empty
#     using truthy and falsy values.

# Q5. Write a login authentication program using nested conditions.
#     Username: admin
#     Password: 12345

# Q6. Write a program to find the largest of three numbers
#     using nested conditions.

# Q7. Create a simple calculator using match-case.
#     Perform addition, subtraction, multiplication, and division.
#     Handle invalid operators and division by zero.

# Q8. Write a shopping discount calculator.
#     Amount >= 5000: 20% discount
#     Amount >= 2000: 10% discount
#     Amount < 2000: No discount
#     Display the discount and final payable amount.

# Q9. Create an ATM withdrawal program.
#     Check whether the withdrawal amount is positive and does not
#     exceed the available balance.
#     Display the remaining balance for a valid transaction.

# Q10. Write a program to check whether a student passes or fails.
#      Accept marks for three subjects.
#      Each mark must be between 0 and 100.
#      The student must score at least 35 in every subject to pass.

# Q11. Create a menu-driven program using match-case.
#      1. Check Even or Odd
#      2. Check Positive, Negative, or Zero
#      3. Find the Square of a Number
#      4. Exit

# Q12. Check whether each value in the following list is truthy or falsy.
#      values = [0, 10, "", "Python", None, False, True, " "]


# ==================================================
# PRACTICE INSTRUCTIONS
# ==================================================

# 1. First, try to solve all the questions yourself.
# 2. Do not look at the solutions immediately.
# 3. Use correct syntax and indentation.
# 4. Test your programs with different inputs.
# 5. If you cannot solve a question, check its solution.
# 6. Understand the logic before moving to the next question.
# 7. Practise writing the code without copying the solution.


# ==================================================
# PART 2: SOLUTIONS
# ==================================================


# ==================================================
# Q1. Voting Eligibility
# ==================================================

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")


# ==================================================
# Q2. Positive, Negative, or Zero
# ==================================================

num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# ==================================================
# Q3. Adult or Minor Using Ternary Operator
# ==================================================

age = int(input("Enter your age: "))

status = "Adult" if age >= 18 else "Minor"

print(status)


# ==================================================
# Q4. Check an Empty or Non-Empty String
# ==================================================

text = input("Enter a string: ")

if text:
    print("String is Not Empty")
else:
    print("String is Empty")


# ==================================================
# Q5. Login Authentication System
# ==================================================

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "12345":
        print("Login Successful")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")


# ==================================================
# Q6. Find the Largest of Three Numbers
# ==================================================

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b:
    if a >= c:
        largest = a
    else:
        largest = c
else:
    if b >= c:
        largest = b
    else:
        largest = c

print("Largest number is:", largest)


# ==================================================
# Q7. Simple Calculator Using match-case
# ==================================================

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

match operator:
    case "+":
        print("Result:", a + b)

    case "-":
        print("Result:", a - b)

    case "*":
        print("Result:", a * b)

    case "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")

    case _:
        print("Invalid Operator")


# ==================================================
# Q8. Shopping Discount Calculator
# ==================================================

amount = float(input("Enter shopping amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
else:
    discount = 0

final_amount = amount - discount

print("Discount:", discount)
print("Final Payable Amount:", final_amount)


# ==================================================
# Q9. ATM Withdrawal System
# ==================================================

balance = float(input("Enter account balance: "))
withdrawal = float(input("Enter withdrawal amount: "))

if withdrawal <= 0:
    print("Invalid withdrawal amount")
else:
    if withdrawal <= balance:
        balance = balance - withdrawal
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance")


# ==================================================
# Q10. Student Pass or Fail
# ==================================================

m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))

if 0 <= m1 <= 100 and 0 <= m2 <= 100 and 0 <= m3 <= 100:
    if m1 >= 35 and m2 >= 35 and m3 >= 35:
        print("Pass")
    else:
        print("Fail")
else:
    print("Invalid Marks")


# ==================================================
# Q11. Menu-Driven Program Using match-case
# ==================================================

print("1. Check Even or Odd")
print("2. Check Positive, Negative, or Zero")
print("3. Find Square")
print("4. Exit")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        num = int(input("Enter a number: "))

        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")

    case 2:
        num = float(input("Enter a number: "))

        if num > 0:
            print("Positive")
        elif num < 0:
            print("Negative")
        else:
            print("Zero")

    case 3:
        num = float(input("Enter a number: "))
        print("Square:", num ** 2)

    case 4:
        print("Exiting Program")

    case _:
        print("Invalid Choice")


# ==================================================
# Q12. Truthy and Falsy Values
# ==================================================

values = [0, 10, "", "Python", None, False, True, " "]

for value in values:
    if value:
        print(repr(value), "-> Truthy")
    else:
        print(repr(value), "-> Falsy")


# ==================================================
# DAY 07 COMPLETION GOAL
# ==================================================

# 1. Understand nested conditions.
# 2. Practise the ternary operator.
# 3. Implement programs using match-case.
# 4. Understand truthy and falsy values.
# 5. Solve all 12 questions independently.
```
