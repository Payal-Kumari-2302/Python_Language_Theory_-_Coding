```python
# Python 90 Days Challenge
# Day 21 - Modules and Packages Practice Questions

# ==============================
# PRACTICE QUESTIONS
# ==============================

# Q1. Import the math module and calculate the square root of 144.

# Q2. Import the math module using an alias and calculate the factorial of 5.

# Q3. Import only the sqrt() function from the math module
#     and calculate the square root of 81.

# Q4. Import the random module and generate a random integer
#     between 1 and 100.

# Q5. Import the datetime module and print the current date and time.

# Q6. Import the statistics module and calculate the mean
#     of the numbers [10, 20, 30, 40, 50].

# Q7. Import the statistics module and calculate the median
#     of the numbers [12, 5, 8, 20, 15].

# Q8. Import the math module and use dir() to display
#     the available names in the module.

# Q9. Create a module named calculator.py containing add()
#     and subtract() functions. Import the module into main.py
#     and call both functions.

# Q10. Create a module named greetings.py containing a greet(name)
#      function. Import the function into main.py and call it.

# Q11. Import the math module using the alias m and calculate
#      the square root of 225.

# Q12. Use if __name__ == "__main__": to print
#      "Program executed directly."

# Q13. Create a module named message.py containing a message variable.
#      Import the variable into main.py and print it.

# Q14. Create a package named mypackage containing addition.py
#      and multiplication.py. Import and use both functions.

# Q15. Import the os module and display the current working directory.

# Q16. Import the sys module and display the Python version.

# Q17. Write the commands to create a virtual environment named myenv
#      and activate it on Windows.

# Q18. Write the command to install the requests package using pip.

# Q19. Write the command to save installed packages
#      into a requirements.txt file.

# Q20. Write the command to install packages listed
#      in requirements.txt.

# Q21. Create a module named student.py containing a function
#      display_student(name, course). Import and call the function.

# Q22. Create a utilities package containing calculator.py
#      and greetings.py. Import and use functions from both modules.

# Q23. Use __name__ == "__main__" to check whether a file
#      is being executed directly or imported.

# Q24. Create an area.py module containing functions to calculate
#      the area of a square and a rectangle. Import and call them.

# Q25. Create a mini project containing main.py, a custom module,
#      and a package with two modules and an __init__.py file.
#      Import and use the functions in main.py.


# ==============================
# PRACTICE INSTRUCTION
# ==============================

# First, try to solve all the questions yourself.
#
# Do not look at the solution immediately.
#
# If you cannot solve a question, check the solution
# and understand the code.
#
# Note:
# Questions involving custom modules and packages require
# separate Python files. Do not put all their code into
# a single file.


# ==============================
# SOLUTIONS
# ==============================

# Q1. Solution

import math

print("Square Root:", math.sqrt(144))


# Q2. Solution

import math as m

print("Factorial:", m.factorial(5))


# Q3. Solution

from math import sqrt

print("Square Root:", sqrt(81))


# Q4. Solution

import random

number = random.randint(1, 100)

print("Random Number:", number)


# Q5. Solution

import datetime

current = datetime.datetime.now()

print("Current Date and Time:", current)


# Q6. Solution

import statistics

numbers = [10, 20, 30, 40, 50]

print("Mean:", statistics.mean(numbers))


# Q7. Solution

import statistics

numbers = [12, 5, 8, 20, 15]

print("Median:", statistics.median(numbers))


# Q8. Solution

import math

print(dir(math))


# Q9. Solution
# Create two separate files: calculator.py and main.py.
#
# calculator.py:
#
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# main.py:

import calculator

print("Addition:", calculator.add(10, 5))
print("Subtraction:", calculator.subtract(10, 5))


# Q10. Solution
# Create greetings.py:
#
# def greet(name):
#     return f"Hello, {name}! Welcome to Python."
#
# main.py:

from greetings import greet

print(greet("Payal"))


# Q11. Solution

import math as m

print("Square Root:", m.sqrt(225))


# Q12. Solution
# Save this code in main.py.

def display():
    print("Program executed directly.")


if __name__ == "__main__":
    display()


# Q13. Solution
# Create message.py:
#
# message = "Welcome to Python"
#
# main.py:

from message import message

print(message)


# Q14. Solution
# Create this package structure:
#
# mypackage/
#     __init__.py
#     addition.py
#     multiplication.py
#
# addition.py:
#
# def add(a, b):
#     return a + b
#
# multiplication.py:
#
# def multiply(a, b):
#     return a * b
#
# main.py:

from mypackage.addition import add
from mypackage.multiplication import multiply

print("Addition:", add(4, 6))
print("Multiplication:", multiply(4, 6))


# Q15. Solution

import os

print("Current Working Directory:", os.getcwd())


# Q16. Solution

import sys

print("Python Version:", sys.version)


# Q17. Solution
# Run these commands in the Windows terminal.
#
# Create virtual environment:
# python -m venv myenv
#
# Activate virtual environment:
# myenv\Scripts\activate
#
# Deactivate virtual environment:
# deactivate


# Q18. Solution
# Run this command in the terminal.
#
# python -m pip install requests


# Q19. Solution
# Run this command in the terminal.
#
# python -m pip freeze > requirements.txt


# Q20. Solution
# Run this command in the terminal.
#
# python -m pip install -r requirements.txt


# Q21. Solution
# Create student.py:
#
# def display_student(name, course):
#     print("Name:", name)
#     print("Course:", course)
#
# main.py:

from student import display_student

display_student("Payal", "BCA")


# Q22. Solution
# Create this package structure:
#
# utilities/
#     __init__.py
#     calculator.py
#     greetings.py
#
# calculator.py:
#
# def multiply(a, b):
#     return a * b
#
# greetings.py:
#
# def greet(name):
#     return f"Hello, {name}!"
#
# main.py:

from utilities.calculator import multiply
from utilities.greetings import greet

print(greet("Payal"))
print("Multiplication:", multiply(5, 4))


# Q23. Solution
# Save this code in check.py.

print("Module Name:", __name__)

if __name__ == "__main__":
    print("File is executed directly.")
else:
    print("File is imported.")


# Q24. Solution
# Create area.py:
#
# def square_area(side):
#     return side * side
#
# def rectangle_area(length, width):
#     return length * width
#
# main.py:

from area import square_area, rectangle_area

print("Square Area:", square_area(5))
print("Rectangle Area:", rectangle_area(6, 4))


# Q25. Solution
# Create this project structure:
#
# mini_project/
#     main.py
#     student.py
#     utilities/
#         __init__.py
#         calculator.py
#         greetings.py
#
# student.py:
#
# def display_student(name):
#     return f"Student Name: {name}"
#
# utilities/calculator.py:
#
# def add(a, b):
#     return a + b
#
# utilities/greetings.py:
#
# def greet(name):
#     return f"Welcome, {name}!"
#
# utilities/__init__.py:
#     # Package initialization file
#
# main.py:

from student import display_student
from utilities.calculator import add
from utilities.greetings import greet

print(display_student("Payal"))
print(greet("Payal"))
print("Sum:", add(10, 20))
```
