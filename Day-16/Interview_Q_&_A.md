# Python 90 Days Challenge

## Day 16 – Collections Module

### Interview Questions & Answers

**Q1. What is the Collections Module?**
**Answer:** A built-in Python module that provides specialized container data types.
**Example:** `Counter`, `deque`

**Q2. What is Counter?**
**Answer:** `Counter` counts how many times each element occurs.
**Example:**

```python
from collections import Counter
print(Counter("hello"))
```

Output: `{'l': 2, 'h': 1, 'e': 1, 'o': 1}`

**Q3. What is defaultdict?**
**Answer:** `defaultdict` automatically provides a default value for a missing key.
**Example:**

```python
from collections import defaultdict
d = defaultdict(int)
d["a"] += 1
print(d["a"])
```

Output: `1`

**Q4. What is OrderedDict?**
**Answer:** `OrderedDict` remembers insertion order and provides extra methods for managing key order.
**Example:**

```python
from collections import OrderedDict
d = OrderedDict([("a", 1), ("b", 2)])
print(d)
```

Output: `OrderedDict([('a', 1), ('b', 2)])`

**Q5. What is deque?**
**Answer:** `deque` is a double-ended queue that allows efficient insertion and removal from both ends.
**Example:**

```python
from collections import deque
q = deque([1, 2, 3])
q.appendleft(0)
print(q)
```

Output: `deque([0, 1, 2, 3])`

**Q6. What is ChainMap?**
**Answer:** `ChainMap` groups multiple dictionaries into one lookup view without merging them into a new dictionary.
**Example:**

```python
from collections import ChainMap
a = {"x": 1}
b = {"y": 2}
c = ChainMap(a, b)
print(c["y"])
```

Output: `2`

**Q7. What is most_common() in Counter?**
**Answer:** It returns elements ordered by their frequency, from highest to lowest.
**Example:**

```python
Counter("aabbbc").most_common(1)
```

Output: `[('b', 3)]`

**Q8. What is default_factory?**
**Answer:** It specifies how `defaultdict` creates a value for a missing key.
**Example:**

```python
defaultdict(list)
```

It creates an empty list for a missing key.

**Q9. What is appendleft() in deque?**
**Answer:** It adds an element to the left end of a deque.
**Example:**

```python
q = deque([2, 3])
q.appendleft(1)
```

Result: `deque([1, 2, 3])`

**Q10. What is move_to_end() in OrderedDict?**
**Answer:** It moves an existing key to the beginning or end of an `OrderedDict`.
**Example:**

```python
d = OrderedDict([("a", 1), ("b", 2)])
d.move_to_end("a")
```

Result: `OrderedDict([('b', 2), ('a', 1)])`

**Q11. What is popleft() in deque?**
**Answer:** It removes and returns the leftmost element.
**Example:**

```python
q = deque([1, 2, 3])
q.popleft()
```

Result: `1`

**Q12. What is the main use of ChainMap?**
**Answer:** It is used to search multiple mappings in order, such as layered configuration settings.
**Example:**

```python
ChainMap({"x": 1}, {"y": 2})
```

It searches the first dictionary before the second.
