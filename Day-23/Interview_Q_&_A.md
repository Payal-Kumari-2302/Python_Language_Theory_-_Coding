# 🐍 PYTHON 90 DAYS CHALLENGE

# DAY-23: PYTHON INTERVIEW QUESTIONS

### BCA Fresher Preparation

## Q1. What is a Class in Python?

**Definition:** A class is a blueprint for creating objects.

**Real-World Example:** A house plan is like a class. It defines how a house can be built.

**Python Example:**

```python
class Student:
    pass
```

## Q2. What is an Object in Python?

**Definition:** An object is an instance of a class.

**Real-World Example:** A student named Payal is an object of the `Student` class.

**Python Example:**

```python
class Student:
    pass

s1 = Student()
```

## Q3. What is the Difference Between a Class and an Object?

**Definition:**

* **Class:** A blueprint for creating objects.
* **Object:** An instance created from a class.

**Real-World Example:** A house plan is a class, while a house built from that plan is an object.

## Q4. How Do You Create a Class in Python?

**Definition:** The `class` keyword is used to define a class in Python.

**Real-World Example:** We can create a `Car` class to represent cars.

**Python Example:**

```python
class Car:
    pass
```

## Q5. How Do You Create an Object of a Class?

**Definition:** An object is created by calling the class name.

**Real-World Example:** Creating a particular student record from a student class.

**Python Example:**

```python
class Student:
    pass

s1 = Student()
```

## Q6. What Are Attributes in Python?

**Definition:** Attributes are variables associated with a class or an object.

**Real-World Example:** A student can have attributes such as name, age, and roll number.

**Python Example:**

```python
class Student:
    name = "Payal"
    age = 21
```

## Q7. What Are Methods in Python?

**Definition:** Methods are functions defined inside a class.

**Real-World Example:** A bank account may have methods such as deposit and withdraw.

**Python Example:**

```python
class Student:
    def display(self):
        print("Student Details")
```

## Q8. What Is `self` in Python?

**Definition:** `self` refers to the current object of a class inside an instance method.

**Real-World Example:** It helps each student object access its own name and age.

**Python Example:**

```python
class Student:
    def __init__(self, name):
        self.name = name
```

## Q9. What Is the `__init__()` Method?

**Definition:** `__init__()` initializes an object's attributes when the object is created.

**Real-World Example:** When creating a student record, we can initialize the student's name and age.

**Python Example:**

```python
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Payal")
```

## Q10. What Is an Instance Variable?

**Definition:** An instance variable belongs to a particular object.

**Real-World Example:** Two students can have different names and roll numbers.

**Python Example:**

```python
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Payal")
s2 = Student("Rahul")
```

## Q11. What Is a Class Variable?

**Definition:** A class variable is defined inside a class and is shared by its objects unless overridden.

**Real-World Example:** Students in the same class may share the same college name.

**Python Example:**

```python
class Student:
    college = "ABC College"

s1 = Student()
s2 = Student()

print(s1.college)
print(s2.college)
```

## Q12. What Is the Difference Between Instance Variables and Class Variables?

**Definition:**

* **Instance variable:** Stores data specific to an object.
* **Class variable:** Stores data shared by objects of a class.

**Real-World Example:**

* Student name: Instance variable.
* College name: Class variable.

## Q13. What Is the Difference Between a Function and a Method?

**Definition:**

* **Function:** A reusable block of code that can be defined independently.
* **Method:** A function defined inside a class.

**Real-World Example:** A standalone calculation function is a function; a `deposit()` operation defined inside a bank account class is a method.

**Python Example:**

```python
def greet():
    print("Hello")

class Student:
    def display(self):
        print("Student")
```

## Q14. Can We Create Multiple Objects from One Class?

**Definition:** Yes, we can create multiple objects from the same class.

**Real-World Example:** A college system can create separate objects for hundreds of students.

**Python Example:**

```python
class Student:
    pass

s1 = Student()
s2 = Student()
s3 = Student()
```

## Q15. How Do You Access an Object's Attributes and Methods?

**Definition:** We generally use the dot (`.`) operator to access an object's attributes and methods.

**Real-World Example:** Accessing a student's name or displaying their details.

**Python Example:**

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

s1 = Student("Payal")
print(s1.name)
s1.display()
```

## Q16. What Is the `pass` Statement in a Class?

**Definition:** `pass` is a placeholder statement that does nothing.

**Real-World Example:** When planning a student management system, we can define the class structure before implementing its features.

**Python Example:**

```python
class Student:
    pass
```

## Q17. Can Objects of the Same Class Have Different Instance Variable Values?

**Definition:** Yes, each object can store its own instance variable values.

**Real-World Example:** Two students can have different names even though both belong to the `Student` class.

**Python Example:**

```python
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Payal")
s2 = Student("Rahul")

print(s1.name)
print(s2.name)
```

## Q18. Can We Access a Class Variable Using an Object?

**Definition:** Yes, a class variable can generally be accessed through an object or the class name.

**Real-World Example:** Students can access their college's shared name.

**Python Example:**

```python
class Student:
    college = "ABC College"

s1 = Student()
print(s1.college)
print(Student.college)
```

## Q19. What Happens If an Instance Variable and a Class Variable Have the Same Name?

**Definition:** An instance attribute generally takes precedence when accessed through that object.

**Real-World Example:** A college may have a default course name, but one student record can store a different course name.

**Python Example:**

```python
class Student:
    course = "BCA"

s1 = Student()
s1.course = "MCA"

print(s1.course)
print(Student.course)
```

**Output:**

```text
MCA
BCA
```

## Q20. Write a Python Program to Create a Student Class with a Display Method.

**Definition:** A class groups related data and methods together.

**Real-World Example:** A college system stores a student's name and displays it when required.

**Python Example:**

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)

s1 = Student("Payal")
s1.display()
```

**Output:**

```text
Student Name: Payal
```
