```python
# Python 90 Days Challenge
# Day-21 - Coding Practice Questions & Solutions

# Python 90 Days Challenge
# Day-21 - Practice


# Q1. Create a local variable inside a function and print it.

# Q2. Create a global variable outside a function and access it
#     inside the function.

# Q3. Create local and global variables with the same name.
#     Print both values to demonstrate variable shadowing.

# Q4. Use the global keyword to modify a global variable
#     inside a function.

# Q5. Create an outer function with a variable and access
#     that variable inside an inner function.

# Q6. Use the nonlocal keyword to modify a variable
#     inside a nested function.

# Q7. Create a nested function to demonstrate the LEGB rule
#     using local, enclosing, and global variables with
#     the same name.

# Q8. Use the len(), max(), min(), and sum() built-in
#     functions on a list of numbers.

# Q9. Create a variable and display the local namespace
#     using the locals() function inside a function.

# Q10. Create global variables and display the global
#      namespace using the globals() function.

# Q11. Write a program to demonstrate the difference
#      between locals() and globals().

# Q12. Write a program that produces a NameError by
#      accessing an undefined variable.

# Q13. Write a program to demonstrate UnboundLocalError
#      by accessing a local variable before assigning it.

# Q14. Create a function that increases a global counter
#      by 1 each time the function is called.

# Q15. Create an outer function with a counter variable.
#      Use an inner function and nonlocal to increase
#      the counter by 1 each time it is called.


# ==========================================
# PRACTICE INSTRUCTION
# ==========================================
# First, try to solve all the questions yourself.
# Do not look at the solution immediately.
# If you cannot solve a question, check the solution
# and understand the logic before moving forward.


# ==================================================
# Q1. Create a local variable inside a function and print it.
# ==================================================

def show_local():
    x = 10
    print(x)

show_local()


# ==================================================
# Q2. Create a global variable outside a function and
# access it inside the function.
# ==================================================

name = "Payal"

def show_global():
    print(name)

show_global()


# ==================================================
# Q3. Create local and global variables with the same name
# to demonstrate variable shadowing.
# ==================================================

x = 100

def show_shadowing():
    x = 50
    print("Local:", x)

show_shadowing()
print("Global:", x)


# ==================================================
# Q4. Use the global keyword to modify a global variable.
# ==================================================

count = 0

def increase_count():
    global count
    count += 1

increase_count()
print(count)


# ==================================================
# Q5. Access an outer function's variable inside an
# inner function.
# ==================================================

def outer():
    message = "Hello Python"

    def inner():
        print(message)

    inner()

outer()


# ==================================================
# Q6. Use the nonlocal keyword to modify an outer variable.
# ==================================================

def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)

outer()


# ==================================================
# Q7. Demonstrate the LEGB rule using local, enclosing,
# and global variables with the same name.
# ==================================================

x = "Global"

def outer():
    x = "Enclosing"

    def inner():
        x = "Local"
        print(x)

    inner()

outer()


# ==================================================
# Q8. Use len(), max(), min(), and sum() on a list.
# ==================================================

numbers = [10, 20, 30, 40]

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))


# ==================================================
# Q9. Display the local namespace using locals().
# ==================================================

def show_locals():
    name = "Payal"
    age = 21
    print(locals())

show_locals()


# ==================================================
# Q10. Display global variables using globals().
# ==================================================

name = "Payal"
course = "Python"

print(globals()["name"])
print(globals()["course"])


# ==================================================
# Q11. Demonstrate the difference between locals()
# and globals().
# ==================================================

x = 100

def show_namespaces():
    y = 200
    print("Local Namespace:", locals())
    print("Global Variable x:", globals()["x"])

show_namespaces()


# ==================================================
# Q12. Demonstrate NameError by accessing an undefined
# variable.
# ==================================================

# Uncomment the next line to test the error.
# print(age)

# Output:
# NameError: name 'age' is not defined


# ==================================================
# Q13. Demonstrate UnboundLocalError by accessing a
# local variable before assigning it.
# ==================================================

# Uncomment the following lines to test the error.
#
# x = 10
#
# def show_error():
#     print(x)
#     x = 20
#
# show_error()

# Output:
# UnboundLocalError


# ==================================================
# Q14. Increase a global counter by 1 each time
# the function is called.
# ==================================================

count = 0

def increase_counter():
    global count
    count += 1

increase_counter()
increase_counter()
increase_counter()

print(count)


# ==================================================
# Q15. Use nonlocal to increase an outer function's
# counter each time the inner function is called.
# ==================================================

def outer():
    count = 0

    def increase_counter():
        nonlocal count
        count += 1
        print(count)

    increase_counter()
    increase_counter()
    increase_counter()

outer()
```


