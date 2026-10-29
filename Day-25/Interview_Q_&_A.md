# Python 90 Days Challenge – Day 25

## Python Interview Questions: MRO to `super()`

### 1. What is MRO?

**Definition:** MRO (Method Resolution Order) defines the order in which Python searches for methods.

**Real-World Example:** In a family, a child may look for help from their mother first, then their father.

```python
class Father:
    def show(self):
        print("Father")

class Child(Father):
    pass

Child().show()
```

**Output:**

```text
Father
```

### 2. What is Multiple Inheritance?

**Definition:** Multiple inheritance allows a child class to inherit from more than one parent class.

**Real-World Example:** A child inherits qualities from both parents.

```python
class Father:
    def skills(self):
        print("Coding")

class Mother:
    def hobby(self):
        print("Cooking")

class Child(Father, Mother):
    pass

obj = Child()
obj.skills()
obj.hobby()
```

**Output:**

```text
Coding
Cooking
```

### 3. What is the Diamond Problem?

**Definition:** The Diamond Problem occurs when a class inherits from two classes that share the same base class.

**Real-World Example:** Two managers inherit from the same company policy, and an employee inherits from both managers.

```python
class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

D().show()
```

**Output:**

```text
A
```

### 4. What is C3 Linearization?

**Definition:** C3 Linearization is the algorithm Python uses to determine the MRO.

**Real-World Example:** It creates a consistent order for deciding which class's method should be called first.

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())
```

### 5. What is `super()`?

**Definition:** `super()` calls the next method in the MRO.

**Real-World Example:** An employee asks the next person in the management chain for assistance.

```python
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def display(self):
        super().show()

Child().display()
```

**Output:**

```text
Parent
```

### 6. What is `super().__init__()`?

**Definition:** It calls the next constructor in the MRO to initialize inherited attributes.

**Real-World Example:** A student record uses a person's name initialized by the parent class.

```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name):
        super().__init__(name)

s = Student("Payal")
print(s.name)
```

**Output:**

```text
Payal
```

### 7. Does `super()` Always Call the Direct Parent?

**Definition:** No. It calls the next class in the MRO.

**Real-World Example:** A request follows the next person in an established chain rather than always going directly to the main manager.

```python
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

B().show()
```

**Output:**

```text
B
A
```

### 8. Does the Parent Constructor Run Automatically?

**Definition:** If a child defines its own `__init__()`, the parent constructor is not called automatically.

**Real-World Example:** A student class must explicitly initialize the person's details when defining its own constructor.

```python
class Person:
    def __init__(self):
        print("Person created")

class Student(Person):
    def __init__(self):
        super().__init__()
        print("Student created")

Student()
```

**Output:**

```text
Person created
Student created
```

---

**Day 25 Complete | Python Interview Preparation**
