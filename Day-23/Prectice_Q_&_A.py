```python
# Python 90 Days Challenge

# Day-23 - Classes and Objects Practice Questions & Solutions


# Q1. Create a Student class and create an object of that class.

# Q2. Create a Student class with name and age attributes.
#     Initialize them using __init__() and display their values.

# Q3. Create a Student class with a display() method.
#     Use self to display the student's name.

# Q4. Create two Student objects with different names.
#     Display the names of both students.

# Q5. Create a Student class with a class variable college = "ABC College".
#     Access it using an object and the class name.

# Q6. Create a Student class with an instance variable name
#     and a class variable college. Display both values.

# Q7. Create a class with a method that prints "Hello, Python".
#     Call the method using an object.

# Q8. Create a class with a class variable course = "BCA".
#     Assign "MCA" to the course attribute of one object.
#     Print the object's course and the class variable's course.

# Q9. Create a function and a class method that both print a message.
#     Call both and observe the difference.

# Q10. Create an Employee class using __init__() to initialize
#      employee name and salary. Display both using a method.


# ==========================================

# PRACTICE INSTRUCTION

# ==========================================

# First, try to solve all the questions yourself.

# Do not look at the solution immediately.

# If you cannot solve a question, check the solution
# and understand the logic before moving forward.


# ==================================================

# Q1. Create a Student class and create an object.

# ==================================================

class Student:
    pass

s1 = Student()

print(s1)


# ==================================================

# Q2. Initialize name and age using __init__().

# ==================================================

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Payal", 21)

s1.display()


# ==================================================

# Q3. Use self to display the student's name.

# ==================================================

class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)

s1 = Student("Payal")

s1.display()


# ==================================================

# Q4. Create two Student objects with different names.

# ==================================================

class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

s1 = Student("Payal")
s2 = Student("Rahul")

s1.display()
s2.display()


# ==================================================

# Q5. Create a class variable named college.

# ==================================================

class Student:
    college = "ABC College"

s1 = Student()

print("Using Object:", s1.college)
print("Using Class:", Student.college)


# ==================================================

# Q6. Use an instance variable and a class variable.

# ==================================================

class Student:
    college = "ABC College"

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)
        print("College:", self.college)

s1 = Student("Payal")

s1.display()


# ==================================================

# Q7. Create a method that prints "Hello, Python".

# ==================================================

class Demo:
    def display(self):
        print("Hello, Python")

obj = Demo()

obj.display()


# ==================================================

# Q8. Change the course attribute for one object.

# ==================================================

class Student:
    course = "BCA"

s1 = Student()

s1.course = "MCA"

print("Object Course:", s1.course)
print("Class Course:", Student.course)


# ==================================================

# Q9. Demonstrate the difference between a function and a method.

# ==================================================

def greet():
    print("Hello from Function")

class Student:
    def display(self):
        print("Hello from Method")

greet()

s1 = Student()
s1.display()


# ==================================================

# Q10. Create an Employee class with name and salary.

# ==================================================

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)

e1 = Employee("Payal", 25000)

e1.display()
```
