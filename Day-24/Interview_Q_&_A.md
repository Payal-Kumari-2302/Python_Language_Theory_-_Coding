# 🐍 Day-24: Python 90 Days Challenge

## OOP Interview Questions with Real-World Examples

This document contains important Python Object-Oriented Programming (OOP) interview questions with simple definitions, real-world examples, Python code, and outputs.

---

## 1. What is OOP?

**Definition:** OOP stands for Object-Oriented Programming. It is a programming approach based on classes and objects.

**Real-World Example:** A car has properties such as color and model and behaviors such as starting and stopping.

```python
class Car:
    def start(self):
        print("Car is starting")

car1 = Car()
car1.start()
```

**Output:**

```text
Car is starting
```

---

## 2. What is Inheritance?

**Definition:** Inheritance allows a child class to use the properties and methods of a parent class.

**Real-World Example:** A Dog can inherit common behavior, such as eating, from an Animal class.

```python
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

dog = Dog()
dog.eat()
dog.bark()
```

**Output:**

```text
Animal is eating
Dog is barking
```

---

## 3. What is Single Inheritance?

**Definition:** Single inheritance occurs when one child class inherits from one parent class.

**Real-World Example:** A Car class inherits from a Vehicle class.

```python
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

car = Car()
car.move()
car.drive()
```

**Output:**

```text
Vehicle is moving
Car is driving
```

---

## 4. What is Multilevel Inheritance?

**Definition:** Multilevel inheritance occurs when classes inherit from one another in a chain.

**Real-World Example:** Puppy inherits from Dog, and Dog inherits from Animal.

```python
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Puppy(Dog):
    def play(self):
        print("Playing")

puppy = Puppy()
puppy.eat()
puppy.bark()
puppy.play()
```

**Output:**

```text
Eating
Barking
Playing
```

---

## 5. What is Hierarchical Inheritance?

**Definition:** Hierarchical inheritance occurs when multiple child classes inherit from the same parent class.

**Real-World Example:** Car and Bike inherit common features from a Vehicle class.

```python
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

car = Car()
bike = Bike()

car.move()
bike.move()
```

**Output:**

```text
Vehicle is moving
Vehicle is moving
```

---

## 6. What is Multiple Inheritance?

**Definition:** Multiple inheritance occurs when one child class inherits from more than one parent class.

**Real-World Example:** A SmartPhone combines features from Phone and Camera classes.

```python
class Phone:
    def call(self):
        print("Making a call")

class Camera:
    def take_photo(self):
        print("Taking a photo")

class SmartPhone(Phone, Camera):
    pass

mobile = SmartPhone()
mobile.call()
mobile.take_photo()
```

**Output:**

```text
Making a call
Taking a photo
```

---

## 7. What is Hybrid Inheritance?

**Definition:** Hybrid inheritance is a combination of two or more types of inheritance.

**Real-World Example:** In a college management system, Student and Employee inherit from Person, while TeachingAssistant inherits from both Student and Employee.

```python
class Person:
    def show_person(self):
        print("Person")

class Student(Person):
    def study(self):
        print("Studying")

class Employee(Person):
    def work(self):
        print("Working")

class TeachingAssistant(Student, Employee):
    pass

ta = TeachingAssistant()
ta.show_person()
ta.study()
ta.work()
```

**Output:**

```text
Person
Studying
Working
```

---

## 8. What is MRO?

**Definition:** MRO stands for Method Resolution Order. It defines the order in which Python searches for methods in inheritance.

**Real-World Example:** If both Father and Mother have a method with the same name, Python follows MRO to determine which method is called first.

```python
class Father:
    def show(self):
        print("Father")

class Mother:
    def show(self):
        print("Mother")

class Child(Father, Mother):
    pass

obj = Child()
obj.show()
```

**Output:**

```text
Father
```

Python checks Father before Mother because Father appears first in the inheritance list.

---

## 📌 Quick Revision

| Inheritance Type | Real-World Example                                   |
| ---------------- | ---------------------------------------------------- |
| Single           | Car inherits from Vehicle                            |
| Multilevel       | Puppy inherits from Dog, Dog inherits from Animal    |
| Hierarchical     | Car and Bike inherit from Vehicle                    |
| Multiple         | SmartPhone inherits from Phone and Camera            |
| Hybrid           | TeachingAssistant inherits from Student and Employee |

---

## 🎯 Learning Goals

* Understand OOP and inheritance.
* Learn the five major types of inheritance in Python.
* Connect programming concepts with real-world examples.
* Prepare for basic Python interview questions.
* Practice Python code and understand its output.

**Day-24 Progress:** Python 90 Days Challenge 🐍

#Python #PythonProgramming #OOP #Inheritance #CodingPractice #100DaysOfCode #PythonInterviewQuestions #GitHub
