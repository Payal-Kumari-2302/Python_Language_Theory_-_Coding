# Day 11 – Lists in Python

## Coding Practice Questions

#1. Create a list and print all its elements.
#2. Access the first and last elements of a list.
#3. Update an element in a list.
#4. Add elements using append() and extend().
#5. Insert an element using insert().
#6. Remove elements using remove() and pop().
#7. Sort a list in ascending and descending order.
#8. Find the largest and smallest numbers in a list.
#9. Count even and odd numbers in a list.
#10. Remove duplicate elements from a list.

## Instructions

- Solve each question independently.
- Write clean and readable Python code.
- Use meaningful variable names.
- Test your code with different inputs.
- Check solutions only after attempting the questions.

---
# Python 90 Days Challenge
# Day 11: Lists in Python
# Coding Solutions

# Q1. Print all elements
numbers = [10, 20, 30, 40, 50]
print(numbers)


# Q2. First and last elements
numbers = [10, 20, 30, 40, 50]
print("First:", numbers[0])
print("Last:", numbers[-1])


# Q3. Update an element
numbers = [10, 20, 30]
numbers[1] = 99
print(numbers)


# Q4. append() and extend()
numbers = [10, 20, 30]
numbers.append(40)
numbers.extend([50, 60])
print(numbers)


# Q5. insert()
numbers = [10, 20, 40]
numbers.insert(2, 30)
print(numbers)


# Q6. remove() and pop()
numbers = [10, 20, 30, 40]
numbers.remove(20)
removed = numbers.pop()
print("Removed:", removed)
print(numbers)


# Q7. Ascending and descending order
numbers = [40, 10, 30, 20]
print("Ascending:", sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))


# Q8. Largest and smallest
numbers = [25, 10, 45, 5, 30]
print("Largest:", max(numbers))
print("Smallest:", min(numbers))


# Q9. Count even and odd numbers
numbers = [1, 2, 3, 4, 5, 6]
even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even:", even_count)
print("Odd:", odd_count)


# Q10. Remove duplicates
numbers = [10, 20, 10, 30, 20, 40]
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)
