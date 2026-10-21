```python
# Python 90 Days Challenge
# Day 17 - Python Functions Practice Questions & Solutions


# ==========================================
# PRACTICE QUESTIONS
# ==========================================

# Q1. Create a function that prints "Hello, Python!"

# Q2. Create a function that prints your name, course,
#     and college.

# Q3. Create a function that accepts a name as a parameter
#     and prints a greeting message.

# Q4. Create a function that accepts two numbers and
#     prints their sum.

# Q5. Create a function that accepts two numbers and
#     returns their sum.

# Q6. Create a function that accepts a number and checks
#     whether it is even or odd.

# Q7. Create a function that accepts a number and returns
#     its square.

# Q8. Create a function that accepts two numbers and
#     returns the greater number.

# Q9. Create a function that uses a default parameter
#     to print a person's name.

# Q10. Create a function that accepts any number of
#      positional arguments using *args and prints them.

# Q11. Create a function that accepts multiple keyword
#      arguments using **kwargs and prints them.

# Q12. Create a function that returns the factorial
#      of a number.

# Q13. Create a lambda function that calculates the
#      square of a number.

# Q14. Create a function that accepts three numbers
#      and returns their average.

# Q15. Create an empty function using the pass statement.


# ==========================================
# PRACTICE INSTRUCTION
# ==========================================

# First, try to solve all the questions yourself.
# Do not look at the solutions immediately.
# Revise function definition, function calls, parameters,
# arguments, return values, and default parameters.
# Practise *args, **kwargs, and lambda functions.
# Understand the logic before moving forward.


# ==================================================
# Q1. Print Hello, Python!
# ==================================================

def greet():
    print("Hello, Python!")

greet()


# ==================================================
# Q2. Print Personal and College Details
# ==================================================

def student_details():
    print("Name: Payal Kumari")
    print("Course: BCA")
    print("College: Pakur Polytechnic")

student_details()


# ==================================================
# Q3. Function with a Parameter
# ==================================================

def greet_name(name):
    print("Hello", name)

greet_name("Payal")


# ==================================================
# Q4. Function to Print the Sum
# ==================================================

def add(a, b):
    print("Sum:", a + b)

add(10, 20)


# ==================================================
# Q5. Function to Return the Sum
# ==================================================

def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print("Sum:", result)


# ==================================================
# Q6. Check Even or Odd Using a Function
# ==================================================

def check_even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_even_odd(7)


# ==================================================
# Q7. Return the Square of a Number
# ==================================================

def square(number):
    return number * number

result = square(5)
print("Square:", result)


# ==================================================
# Q8. Find the Greater Number
# ==================================================

def greater_number(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Both numbers are equal"

print(greater_number(10, 20))


# ==================================================
# Q9. Function with a Default Parameter
# ==================================================

def greet(name="Payal"):
    print("Hello", name)

greet()
greet("Rahul")


# ==================================================
# Q10. Using *args
# ==================================================

def show_numbers(*args):
    print(args)

show_numbers(10, 20, 30, 40, 50)


# ==================================================
# Q11. Using **kwargs
# ==================================================

def student_info(**kwargs):
    print(kwargs)

student_info(name="Payal", age=21, course="BCA")


# ==================================================
# Q12. Calculate Factorial Using a Function
# ==================================================

def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result = result * i

    return result

print("Factorial:", factorial(5))


# ==================================================
# Q13. Square Using a Lambda Function
# ==================================================

square = lambda number: number * number

print("Square:", square(6))


# ==================================================
# Q14. Calculate the Average of Three Numbers
# ==================================================

def average(a, b, c):
    return (a + b + c) / 3

print("Average:", average(10, 20, 30))


# ==================================================
# Q15. Create an Empty Function
# ==================================================

def future_function():
    pass

print("Empty function defined successfully")
```
