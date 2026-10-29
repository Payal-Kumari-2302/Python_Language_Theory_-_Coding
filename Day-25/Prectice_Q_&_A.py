```python
# Python 90 Days Challenge
# Day 25 - MRO and super() Practice Questions & Solutions


# ==========================================
# PRACTICE QUESTIONS
# ==========================================

# Q1. Create a Parent class with a show() method.
#     Create a Child class and call the inherited method.

# Q2. Create classes A, B, C, and D to demonstrate
#     the Diamond Problem. Print the MRO of class D.

# Q3. Create a Person class with an __init__() method
#     that accepts a name. Create a Student class without
#     its own constructor and print the student's name.

# Q4. Create a Parent class with a show() method.
#     Override the method in the Child class and use
#     super() to call the Parent class method.

# Q5. Create a Person class with a constructor that
#     accepts a name. Create a Student class that accepts
#     a name and course. Use super().__init__() to
#     initialize the name and print both attributes.

# Q6. Create classes A, B, and C where B inherits from A
#     and C inherits from B. Use super() to call the
#     methods and observe the output.


# ==========================================
# PRACTICE INSTRUCTIONS
# ==========================================

# 1. First, try to solve all questions yourself.
# 2. Understand the Method Resolution Order (MRO).
# 3. Practise multiple inheritance and the Diamond Problem.
# 4. Use super() to call the next method in the MRO.
# 5. Practise constructor inheritance.
# 6. Check the output carefully.


# ==================================================
# Q1. Inheritance and MRO
# ==================================================

# Expected Output:
# Parent method called

class Parent:
    def show(self):
        print("Parent method called")

class Child(Parent):
    pass

obj = Child()
obj.show()


# ==================================================
# Q2. Diamond Problem and MRO
# ==================================================

# Expected Output:
# A
# ['D', 'B', 'C', 'A', 'object']

class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

obj = D()
obj.show()

print([cls.__name__ for cls in D.mro()])


# ==================================================
# Q3. Inheriting a Constructor
# ==================================================

# Expected Output:
# Payal

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    pass

s = Student("Payal")
print(s.name)


# ==================================================
# Q4. Using super() to Call a Parent Method
# ==================================================

# Expected Output:
# Child method called
# Parent method called

class Parent:
    def show(self):
        print("Parent method called")

class Child(Parent):
    def show(self):
        print("Child method called")
        super().show()

obj = Child()
obj.show()


# ==================================================
# Q5. Using super().__init__()
# ==================================================

# Expected Output:
# Name: Payal
# Course: BCA

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

s = Student("Payal", "BCA")

print("Name:", s.name)
print("Course:", s.course)


# ==================================================
# Q6. MRO with super()
# ==================================================

# Expected Output:
# B
# C
# A

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(B):
    def show(self):
        print("C")
        super().show()

obj = C()
obj.show()


# ==========================================
# END OF DAY 25 - MRO AND super()
# ==========================================
```
