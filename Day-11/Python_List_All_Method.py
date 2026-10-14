# Day 11 – Lists in Python

## Q1. What does the append() method do?

**Definition:** The `append()` method adds one item to the end of a list.

**Real-World Example:** Adding a new student to a student list.

```python
students = ["Payal", "Riya"]
students.append("Aman")
print(students)
```

## Q2. What does the extend() method do?

**Definition:** The `extend()` method adds all items from an iterable to the end of a list.

**Real-World Example:** Adding students from another class to a student list.

```python
students = ["Payal", "Riya"]
students.extend(["Aman", "Priya"])
print(students)
```

## Q3. What does the insert() method do?

**Definition:** The `insert()` method adds an item at a specified index.

**Real-World Example:** Adding a new task at a specific position in a to-do list.

```python
tasks = ["Study", "Exercise"]
tasks.insert(1, "Practice Python")
print(tasks)
```

## Q4. What does the remove() method do?

**Definition:** The `remove()` method removes the first occurrence of a specified value.

**Real-World Example:** Removing a cancelled item from a shopping list.

```python
shopping = ["Milk", "Bread", "Eggs"]
shopping.remove("Bread")
print(shopping)
```

## Q5. What does the pop() method do?

**Definition:** The `pop()` method removes and returns an item by index. By default, it removes the last item.

**Real-World Example:** Removing the last task from a task list.

```python
tasks = ["Study", "Exercise", "Reading"]
completed = tasks.pop()
print(completed)
print(tasks)
```

## Q6. What does the clear() method do?

**Definition:** The `clear()` method removes all items from a list.

**Real-World Example:** Clearing all items from a temporary shopping list.

```python
shopping = ["Milk", "Bread", "Eggs"]
shopping.clear()
print(shopping)
```

## Q7. What does the index() method do?

**Definition:** The `index()` method returns the index of the first occurrence of a specified value.

**Real-World Example:** Finding the position of a student in a class list.

```python
students = ["Payal", "Riya", "Aman"]
print(students.index("Riya"))
```

## Q8. What does the count() method do?

**Definition:** The `count()` method returns the number of times a value appears in a list.

**Real-World Example:** Counting how many times a product appears in an order list.

```python
orders = ["Pen", "Book", "Pen", "Pencil"]
print(orders.count("Pen"))
```

## Q9. What does the sort() method do?

**Definition:** The `sort()` method sorts the original list in ascending order by default.

**Real-World Example:** Arranging students' marks from lowest to highest.

```python
marks = [75, 90, 60, 85]
marks.sort()
print(marks)
```

## Q10. What does the reverse() method do?

**Definition:** The `reverse()` method reverses the order of items in the original list.

**Real-World Example:** Reversing the order of recent activities.

```python
activities = ["Study", "Eat", "Sleep"]
activities.reverse()
print(activities)
```

## Q11. What does the copy() method do?

**Definition:** The `copy()` method returns a shallow copy of a list.

**Real-World Example:** Creating a separate copy of a shopping list.

```python
shopping = ["Milk", "Bread", "Eggs"]
backup = shopping.copy()
print(backup)
```

## Q12. What does the len() function do with a list?

**Definition:** The `len()` function returns the total number of items in a list.

**Real-World Example:** Counting the number of students in a class.

```python
students = ["Payal", "Riya", "Aman"]
print(len(students))
```

## Q13. What does the sum() function do with a list?

**Definition:** The `sum()` function returns the total of numeric items in a list.

**Real-World Example:** Calculating the total marks obtained by a student.

```python
marks = [80, 90, 85]
print(sum(marks))
```

## Q14. What does the min() function do with a list?

**Definition:** The `min()` function returns the smallest item in a list.

**Real-World Example:** Finding the lowest price among products.

```python
prices = [100, 250, 75, 180]
print(min(prices))
```

## Q15. What does the max() function do with a list?

**Definition:** The `max()` function returns the largest item in a list.

**Real-World Example:** Finding the highest marks in a class.

```python
marks = [70, 95, 82, 88]
print(max(marks))
```

## Q16. What does the sorted() function do with a list?

**Definition:** The `sorted()` function returns a new sorted list without modifying the original list.

**Real-World Example:** Displaying product prices from lowest to highest while keeping the original order unchanged.

```python
prices = [300, 100, 200]
result = sorted(prices)

print(result)
print(prices)
```

## Q17. What does the reverse=True parameter do in sort() and sorted()?

**Definition:** The `reverse=True` parameter sorts items in descending order.

**Real-World Example:** Arranging students' marks from highest to lowest.

```python
marks = [75, 90, 60, 85]

marks.sort(reverse=True)
print(marks)

print(sorted(marks, reverse=True))
```

## Q18. What does the copy() method not do?

**Definition:** The `copy()` method creates a shallow copy; it does not recursively copy nested lists.

**Real-World Example:** Copying student records while understanding that nested lists may still be shared.

```python
students = [["Payal", 90], ["Riya", 85]]
backup = students.copy()

print(backup)
```
