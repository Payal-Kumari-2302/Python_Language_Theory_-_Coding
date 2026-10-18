
```python
# Python 90 Days Challenge
# Day 14 - Practice Questions

# ==============================
# PRACTICE QUESTIONS
# ==============================

# Q1. Create a dictionary containing your name, age, and course.
#     Print the dictionary.

# Q2. Create a student dictionary and print only the student's name
#     and course.

# Q3. Add a new key "city" to an existing student dictionary.

# Q4. Update an employee's salary in a dictionary.

# Q5. Remove the "age" key from a dictionary using pop().

# Q6. Check whether the key "email" exists in a dictionary.

# Q7. Use the get() method to access a key that may not exist.
#     Print "Not Found" if the key is missing.

# Q8. Print all keys and values of an employee dictionary using items().

# Q9. Find the total number of key-value pairs in a dictionary.

# Q10. Create a nested dictionary containing two students' details.
#      Print the first student's marks.

# Q11. Create a dictionary containing numbers from 1 to 5
#      and their squares using dictionary comprehension.

# Q12. Create a dictionary containing only even numbers and their
#      squares from 1 to 10 using dictionary comprehension.

# Q13. Merge two dictionaries using the update() method.

# Q14. Copy a dictionary using copy(). Update the copied dictionary
#      and print both dictionaries.

# Q15. Count the frequency of each character in the string "banana"
#      using a dictionary.


# ==============================
# PRACTICE INSTRUCTION
# ==============================

# First, try to solve all the questions yourself.
# Do not look at the solutions immediately.
# If you cannot solve a question, check the solution
# and understand the code.


# ==============================
# SOLUTIONS
# ==============================

# Q1. Solution
student = {
    "name": "Payal",
    "age": 21,
    "course": "BCA"
}
print(student)


# Q2. Solution
student = {
    "name": "Payal",
    "age": 21,
    "course": "BCA"
}
print(student["name"])
print(student["course"])


# Q3. Solution
student = {
    "name": "Payal",
    "course": "BCA"
}
student["city"] = "Pakur"
print(student)


# Q4. Solution
employee = {
    "name": "Aman",
    "salary": 20000
}
employee["salary"] = 25000
print(employee)


# Q5. Solution
student = {
    "name": "Payal",
    "age": 21,
    "course": "BCA"
}
student.pop("age")
print(student)


# Q6. Solution
student = {
    "name": "Payal",
    "email": "payal@example.com"
}
print("email" in student)


# Q7. Solution
student = {"name": "Payal"}
print(student.get("age", "Not Found"))


# Q8. Solution
employee = {
    "name": "Aman",
    "department": "IT",
    "salary": 25000
}

for key, value in employee.items():
    print(key, ":", value)


# Q9. Solution
student = {
    "name": "Payal",
    "age": 21,
    "course": "BCA",
    "city": "Pakur"
}
print(len(student))


# Q10. Solution
students = {
    "student1": {"name": "Payal", "marks": 85},
    "student2": {"name": "Aman", "marks": 90}
}
print(students["student1"]["marks"])


# Q11. Solution
squares = {n: n ** 2 for n in range(1, 6)}
print(squares)


# Q12. Solution
even_squares = {
    n: n ** 2
    for n in range(1, 11)
    if n % 2 == 0
}
print(even_squares)


# Q13. Solution
student = {
    "name": "Payal",
    "age": 21
}

extra = {
    "course": "BCA",
    "city": "Pakur"
}

student.update(extra)
print(student)


# Q14. Solution
student1 = {
    "name": "Payal",
    "age": 21
}

student2 = student1.copy()
student2["age"] = 22

print("Original:", student1)
print("Copied:", student2)


# Q15. Solution
text = "banana"
frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)
```
