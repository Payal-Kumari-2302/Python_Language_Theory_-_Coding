```python
# Python 90 Days Challenge
# Day 16 - Practice Questions & Solutions

# Python 90 Days Challenge
# Day 16 - Practice

# Topic: Collections Module
# Counter, defaultdict, OrderedDict, deque, ChainMap


# Q1. Count the frequency of each character using Counter.

# Q2. Find the three most common elements in a list using Counter.

# Q3. Count the frequency of each word in a sentence using Counter.

# Q4. Count the frequency of each character using defaultdict(int).

# Q5. Group words by their first character using defaultdict(list).

# Q6. Create an OrderedDict and display its key-value pairs.

# Q7. Move a specified key to the end using move_to_end().

# Q8. Add elements to both ends of a deque.

# Q9. Remove elements from both ends of a deque.

# Q10. Reverse a deque.

# Q11. Combine two dictionaries using ChainMap.

# Q12. Access a key from the second dictionary using ChainMap.

# Q13. Check whether two strings have the same character frequencies using Counter.

# Q14. Count the vowels in a string using Counter.

# Q15. Implement a queue using deque.


# ==========================================
# PRACTICE INSTRUCTION
# ==========================================
# First, try to solve all the questions yourself.
# Do not look at the solution immediately.
# If you cannot solve a question, check the solution
# and understand the logic before moving forward.


# ==================================================
# Q1. Count the frequency of each character using Counter.
# ==================================================

from collections import Counter

text = "banana"

result = Counter(text)

print(result)


# ==================================================
# Q2. Find the three most common elements in a list.
# ==================================================

from collections import Counter

numbers = [1, 2, 2, 3, 3, 3, 4, 4]

result = Counter(numbers)

print(result.most_common(3))


# ==================================================
# Q3. Count the frequency of each word in a sentence.
# ==================================================

from collections import Counter

sentence = "python is easy and python is powerful"

words = sentence.split()

result = Counter(words)

print(result)


# ==================================================
# Q4. Count character frequency using defaultdict(int).
# ==================================================

from collections import defaultdict

text = "apple"

frequency = defaultdict(int)

for char in text:
    frequency[char] += 1

print(dict(frequency))


# ==================================================
# Q5. Group words using defaultdict(list).
# ==================================================

from collections import defaultdict

words = ["apple", "ant", "ball", "bat", "cat"]

groups = defaultdict(list)

for word in words:
    groups[word[0]].append(word)

print(dict(groups))


# ==================================================
# Q6. Create an OrderedDict and display its elements.
# ==================================================

from collections import OrderedDict

data = OrderedDict([
    ("name", "Payal"),
    ("course", "BCA"),
    ("college", "Pakur Polytechnic")
])

print(data)


# ==================================================
# Q7. Move a key to the end using move_to_end().
# ==================================================

from collections import OrderedDict

data = OrderedDict([
    ("a", 1),
    ("b", 2),
    ("c", 3)
])

data.move_to_end("a")

print(data)


# ==================================================
# Q8. Add elements to both ends of a deque.
# ==================================================

from collections import deque

numbers = deque([10, 20, 30])

numbers.appendleft(5)
numbers.append(40)

print(numbers)


# ==================================================
# Q9. Remove elements from both ends of a deque.
# ==================================================

from collections import deque

numbers = deque([10, 20, 30, 40])

numbers.popleft()
numbers.pop()

print(numbers)


# ==================================================
# Q10. Reverse a deque.
# ==================================================

from collections import deque

numbers = deque([1, 2, 3, 4, 5])

numbers.reverse()

print(numbers)


# ==================================================
# Q11. Combine two dictionaries using ChainMap.
# ==================================================

from collections import ChainMap

first = {"a": 10}
second = {"b": 20}

result = ChainMap(first, second)

print(result)


# ==================================================
# Q12. Access a key from the second dictionary.
# ==================================================

from collections import ChainMap

first = {"a": 10}
second = {"b": 20}

result = ChainMap(first, second)

print(result["b"])


# ==================================================
# Q13. Check whether two strings have the same
# character frequencies using Counter.
# ==================================================

from collections import Counter

text1 = "listen"
text2 = "silent"

if Counter(text1) == Counter(text2):
    print("Both strings have the same character frequencies.")
else:
    print("Character frequencies are different.")


# ==================================================
# Q14. Count the vowels in a string using Counter.
# ==================================================

from collections import Counter

text = "education"

vowels = Counter(
    char for char in text.lower()
    if char in "aeiou"
)

print(vowels)


# ==================================================
# Q15. Implement a queue using deque.
# ==================================================

from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

removed = queue.popleft()

print("Removed element:", removed)
print("Remaining queue:", queue)
```
