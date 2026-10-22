```python
# Python 90 Days Challenge
# Day 18 - Practice Questions & Solutions

# Python 90 Days Challenge
# Day 18 - Practice

# Q1. Create a function named greet() that prints "Hello, Python!"

# Q2. Create a function greet_user(name) that prints a personalized greeting.

# Q3. Create a function display_student(name, age) using positional arguments.

# Q4. Create a function add(a, b) that returns the sum of two numbers.

# Q5. Create a function calculate(a, b) that returns the sum, difference,
#     and product of two numbers.

# Q6. Create a function greet(name="Guest") that uses a default parameter.

# Q7. Create a function display_student(name, age) and call it using
#     keyword arguments.

# Q8. Create a function calculate_sum(*args) that returns the sum of
#     any number of numeric arguments.

# Q9. Create a function find_max(*args) that returns the largest number.

# Q10. Create a function display_details(**kwargs) that prints all
#      key-value pairs.

# Q11. Create a function count_details(**kwargs) that returns the number
#      of keyword arguments passed to it.

# Q12. Create a function show_data(*args, **kwargs) that prints positional
#      and keyword arguments separately.

# Q13. Create a function with a required parameter, a default parameter,
#      *args, and **kwargs. Print all received values.

# Q14. Create a function multiply(a, b) with a docstring that returns
#      the product of two numbers.

# Q15. Create a function calculate_average(numbers) that returns the
#      average of a list of numbers.


# ==========================================
# PRACTICE INSTRUCTION
# ==========================================
# First, try to solve all the questions yourself.
# Do not look at the solution immediately.
# If you cannot solve a question, check the solution
# and understand the logic before moving forward.


# ==================================================
# Q1. Create a function named greet() that prints
#     "Hello, Python!"
# ==================================================

def greet():
    print("Hello, Python!")

greet()


# ==================================================
# Q2. Create a function greet_user(name) that prints
#     a personalized greeting.
# ==================================================

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Payal")


# ==================================================
# Q3. Create a function display_student(name, age)
#     using positional arguments.
# ==================================================

def display_student(name, age):
    print("Name:", name)
    print("Age:", age)

display_student("Payal", 21)


# ==================================================
# Q4. Create a function add(a, b) that returns
#     the sum of two numbers.
# ==================================================

def add(a, b):
    return a + b

print(add(10, 20))


# ==================================================
# Q5. Return the sum, difference, and product
#     of two numbers.
# ==================================================

def calculate(a, b):
    return a + b, a - b, a * b

print(calculate(10, 5))


# ==================================================
# Q6. Use a default parameter in a function.
# ==================================================

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Payal")


# ==================================================
# Q7. Call a function using keyword arguments.
# ==================================================

def display_student(name, age):
    print("Name:", name)
    print("Age:", age)

display_student(age=21, name="Payal")


# ==================================================
# Q8. Use *args to calculate the sum of numbers.
# ==================================================

def calculate_sum(*args):
    return sum(args)

print(calculate_sum(10, 20, 30, 40))


# ==================================================
# Q9. Find the largest number using *args.
# ==================================================

def find_max(*args):
    if not args:
        return None
    return max(args)

print(find_max(12, 45, 7, 89, 23))


# ==================================================
# Q10. Use **kwargs to display key-value pairs.
# ==================================================

def display_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_details(name="Payal", age=21, city="Pakur")


# ==================================================
# Q11. Count the keyword arguments using **kwargs.
# ==================================================

def count_details(**kwargs):
    return len(kwargs)

print(count_details(name="Payal", age=21, city="Pakur"))


# ==================================================
# Q12. Display positional and keyword arguments.
# ==================================================

def show_data(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

show_data(10, 20, 30, name="Payal", age=21)


# ==================================================
# Q13. Use a required parameter, default parameter,
#      *args, and **kwargs.
# ==================================================

def show_details(name, age=18, *args, **kwargs):
    print("Name:", name)
    print("Age:", age)
    print("Extra positional arguments:", args)
    print("Extra keyword arguments:", kwargs)

show_details("Payal", 21, "BCA", "Python", city="Pakur")


# ==================================================
# Q14. Create a function with a docstring that
#      returns the product of two numbers.
# ==================================================

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

print(multiply(4, 5))


# ==================================================
# Q15. Calculate the average of a list of numbers.
# ==================================================

def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

print(calculate_average([10, 20, 30]))
```
