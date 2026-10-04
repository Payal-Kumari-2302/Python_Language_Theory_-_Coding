# Python 90 Days Challenge
# Day 02 - Practice Questions

# ==============================
# PRACTICE QUESTIONS
# ==============================

# Q1. Take your name as input and print it.

# Q2. Take your name and age as input and print them.

# Q3. Take two numbers as input and print their sum.

# Q4. Take length and breadth as input and calculate the area of a rectangle.

# Q5. Create variables for your name, course, and college and print them.

# Q6. Swap the values of two variables.

# Q7. Take a number as input and calculate its square and cube.

# Q8. Take two numbers and perform +, -, *, / operations.

# Q9. Take three numbers and calculate their average.

# Q10. Identify which of the given words are Python keywords and which
#      are valid identifiers:
#      if, name, for, student1, class, total_marks


# ==============================
# PRACTICE INSTRUCTION
# ==============================
# First, try to solve all the questions yourself.
# Do not look at the solutions immediately.
# If you cannot solve a question, check the solution
# and understand the code.


# ==============================
# SOLUTIONS
# ==============================

# Q1. Solution
name = input("Enter your name: ")
print("Name:", name)


# Q2. Solution
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Name:", name)
print("Age:", age)


# Q3. Solution
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)


# Q4. Solution
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area:", area)


# Q5. Solution
name = "Payal"
course = "BCA"
college = "Pakur Polytechnic"

print("Name:", name)
print("Course:", course)
print("College:", college)


# Q6. Solution
a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)


# Q7. Solution
number = int(input("Enter a number: "))

print("Square:", number ** 2)
print("Cube:", number ** 3)


# Q8. Solution
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


# Q9. Solution
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

average = (a + b + c) / 3
print("Average:", average)


# Q10. Solution
# Keywords: if, for, class
# Valid identifiers: name, student1, total_marks
