# Python 90 Days Challenge

# Day 03 - Python Data Types Practice Questions

# ==============================

# PRACTICE QUESTIONS

# ==============================

# Q1. Create variables of int, float, complex, and bool data types

# and print their values.

# Q2. Take an integer and a float as input and print their sum.

# Q3. Take a string as input and print the string and its length.

# Q4. Create a list of five numbers and print the list.

# Q5. Create a tuple of five numbers and print the tuple.

# Q6. Create a set containing duplicate values and print the set.

# Observe what happens to the duplicate values.

# Q7. Create a dictionary containing a student's name, age, and course

# and print the dictionary.

# Q8. Create variables of different data types and use type()

# to print the data type of each variable.

# Q9. Create a list and modify one of its elements.

# Then print the updated list.

# Q10. Create two numbers as input and perform addition, subtraction,

# multiplication, and division. Print the result of each operation.

# ==============================

# PRACTICE INSTRUCTION

# ==============================

# First, try to solve all the questions yourself.

# Do not look at the solution immediately.

# If you cannot solve a question, check the solution

# and understand the code.

# ==============================

# SOLUTIONS

# ==============================

# Q1. Solution

a = 10
b = 10.5
c = 3 + 4j
d = True

print("Integer:", a)
print("Float:", b)
print("Complex:", c)
print("Boolean:", d)

# Q2. Solution

a = int(input("Enter an integer: "))
b = float(input("Enter a float: "))

print("Sum:", a + b)

# Q3. Solution

text = input("Enter a string: ")

print("String:", text)
print("Length:", len(text))

# Q4. Solution

numbers = [10, 20, 30, 40, 50]

print("List:", numbers)

# Q5. Solution

numbers = (10, 20, 30, 40, 50)

print("Tuple:", numbers)

# Q6. Solution

numbers = {10, 20, 20, 30, 30, 40}

print("Set:", numbers)

# Q7. Solution

student = {
"name": "Payal",
"age": 21,
"course": "BCA"
}

print("Student:", student)

# Q8. Solution

a = 10
b = 10.5
c = "Python"
d = [1, 2, 3]
e = (1, 2, 3)
f = {1, 2, 3}
g = {"name": "Payal"}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

# Q9. Solution

numbers = [10, 20, 30]

numbers[0] = 100

print("Updated list:", numbers)

# Q10. Solution

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
