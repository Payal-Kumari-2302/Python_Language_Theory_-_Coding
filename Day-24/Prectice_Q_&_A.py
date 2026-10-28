```python
# Python 90 Days Challenge
# Day 24 - OOP and Inheritance
# Coding Practice Questions


# ==============================
# QUESTIONS
# ==============================

# Q1. Create a Person class with name and age.
#     Create an object and display the details.

# Q2. Create an Employee class with name and salary.
#     Display employee details using an object.

# Q3. Create a Vehicle class with a start() method.
#     Create a Car class that inherits from Vehicle.
#     Add a drive() method to Car.

# Q4. Create a Person class with a name attribute.
#     Create an Employee class that inherits from Person.
#     Create a Developer class that inherits from Employee.
#     Display name, employee ID, and programming language.

# Q5. Create a Shape class with a display() method.
#     Create Circle and Rectangle classes that inherit
#     from Shape. Display their respective messages.

# Q6. Create an Animal class with an eat() method.
#     Create Dog and Cat classes that inherit from Animal.
#     Add bark() and meow() methods.

# Q7. Create Father and Mother classes.
#     Add one method to each class.
#     Create a Child class that inherits from both classes.
#     Call both methods using a Child object.

# Q8. Create Camera and MusicPlayer classes.
#     Create a Smartphone class that inherits from both.
#     Display photo and music features.

# Q9. Create classes A, B, C, and D.
#     B and C inherit from A.
#     D inherits from B and C.
#     Display the Method Resolution Order (MRO).

# Q10. Create Father and Mother classes with a show() method.
#      Create a Child class that inherits from both.
#      Call show() and observe which method executes first.

# Q11. Create a Person class.
#      Create Student and Employee classes that inherit
#      from Person.
#      Create a WorkingStudent class that inherits from
#      both Student and Employee.
#      Display the person's name.

# Q12. Create a Device class with a power_on() method.
#      Create Computer and Phone classes that inherit
#      from Device.
#      Create a SmartDevice class that inherits from both.
#      Call power_on() using a SmartDevice object.

# Q13. Create a BankAccount class with an account holder's
#      name and a display_account() method.
#      Create a SavingsAccount class that inherits from it.
#      Add an interest rate and display all details.

# Q14. Create a Person class with a name attribute.
#      Create a Member class that inherits from Person.
#      Create a PremiumMember class that inherits from Member.
#      Display name, member ID, and membership type.

# Q15. Create a Library Management example using inheritance.
#      Create a Person class, a Member class, and a
#      PremiumMember class.
#      Display all member details.


# ==============================
# INSTRUCTIONS
# ==============================

# 1. Read each question carefully.
# 2. Try to solve the questions before checking solutions.
# 3. Understand classes, objects, and inheritance.
# 4. Practise single, multilevel, hierarchical, and
#    multiple inheritance.
# 5. Understand the Method Resolution Order (MRO).
# 6. Use proper indentation.
# 7. Run each program and verify its output.
# 8. Save your practice in the Day-24 folder.


# ==============================
# SOLUTIONS
# ==============================


# Q1. Person class with name and age.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


person = Person("Payal", 21)
person.display()


# Q2. Employee class with name and salary.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee:", self.name)
        print("Salary:", self.salary)


employee = Employee("Rahul", 30000)
employee.display()


# Q3. Single Inheritance.

class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    def drive(self):
        print("Car is moving")


car = Car()
car.start()
car.drive()


# Q4. Multilevel Inheritance.

class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id


class Developer(Employee):
    def __init__(self, name, employee_id, language):
        super().__init__(name, employee_id)
        self.language = language

    def display(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Language:", self.language)


developer = Developer("Payal", 101, "Python")
developer.display()


# Q5. Hierarchical Inheritance.

class Shape:
    def display(self):
        print("This is a shape")


class Circle(Shape):
    def show(self):
        print("This is a circle")


class Rectangle(Shape):
    def show(self):
        print("This is a rectangle")


circle = Circle()
circle.display()
circle.show()

rectangle = Rectangle()
rectangle.display()
rectangle.show()


# Q6. Animal Inheritance.

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def meow(self):
        print("Cat is meowing")


dog = Dog()
dog.eat()
dog.bark()

cat = Cat()
cat.eat()
cat.meow()


# Q7. Multiple Inheritance.

class Father:
    def father_property(self):
        print("Father's property")


class Mother:
    def mother_property(self):
        print("Mother's property")


class Child(Father, Mother):
    pass


child = Child()
child.father_property()
child.mother_property()


# Q8. Smartphone using Multiple Inheritance.

class Camera:
    def take_photo(self):
        print("Taking a photo")


class MusicPlayer:
    def play_music(self):
        print("Playing music")


class Smartphone(Camera, MusicPlayer):
    pass


phone = Smartphone()
phone.take_photo()
phone.play_music()


# Q9. Method Resolution Order (MRO).

class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print("MRO:", D.mro())


# Q10. Understanding MRO.

class Father:
    def show(self):
        print("Father's method")


class Mother:
    def show(self):
        print("Mother's method")


class Child(Father, Mother):
    pass


child = Child()
child.show()

print("MRO:", Child.mro())


# Q11. Hybrid Inheritance.

class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    pass


class Employee(Person):
    pass


class WorkingStudent(Student, Employee):
    def display(self):
        print("Name:", self.name)


student = WorkingStudent("Payal")
student.display()


# Q12. Hybrid Inheritance with Device.

class Device:
    def power_on(self):
        print("Device is powered on")


class Computer(Device):
    pass


class Phone(Device):
    pass


class SmartDevice(Computer, Phone):
    pass


device = SmartDevice()
device.power_on()

print("MRO:", SmartDevice.mro())


# Q13. Banking System.

class BankAccount:
    def __init__(self, name):
        self.name = name

    def display_account(self):
        print("Account Holder:", self.name)


class SavingsAccount(BankAccount):
    def __init__(self, name, interest_rate):
        super().__init__(name)
        self.interest_rate = interest_rate

    def display_details(self):
        self.display_account()
        print("Interest Rate:", self.interest_rate, "%")


account = SavingsAccount("Payal", 5)
account.display_details()


# Q14. Premium Membership.

class Person:
    def __init__(self, name):
        self.name = name


class Member(Person):
    def __init__(self, name, member_id):
        super().__init__(name)
        self.member_id = member_id


class PremiumMember(Member):
    def __init__(self, name, member_id, membership_type):
        super().__init__(name, member_id)
        self.membership_type = membership_type

    def display(self):
        print("Name:", self.name)
        print("Member ID:", self.member_id)
        print("Membership:", self.membership_type)


member = PremiumMember("Payal", 101, "Premium")
member.display()


# Q15. Library Management System.

class Person:
    def __init__(self, name):
        self.name = name


class Member(Person):
    def __init__(self, name, member_id):
        super().__init__(name)
        self.member_id = member_id

    def display(self):
        print("Name:", self.name)
        print("Member ID:", self.member_id)


class PremiumMember(Member):
    def __init__(self, name, member_id, membership_type):
        super().__init__(name, member_id)
        self.membership_type = membership_type

    def display(self):
        super().display()
        print("Membership Type:", self.membership_type)


library_member = PremiumMember("Payal", 101, "Premium")
library_member.display()
```
