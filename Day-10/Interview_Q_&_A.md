# Python 90 Days Challenge

## Day 10 – Interview Questions & Answers

### Topic: Loops and Iterators

### Q1. What is the difference between `break`, `continue`, and `pass`?

**Answer:** `break` stops the loop, `continue` skips the current iteration, and `pass` does nothing.

**Real-world example:** Stopping a search, skipping an absent student, and reserving a task for later.

### Q2. When does a loop's `else` block execute?

**Answer:** It executes when the loop finishes normally without encountering `break`.

**Real-world example:** Displaying "Search completed" after checking all records.

### Q3. What is a nested loop, and where is it used?

**Answer:** A nested loop is a loop inside another loop. It is used for patterns, tables, and rows and columns.

**Real-world example:** Checking students in multiple classrooms.

### Q4. What is the difference between `range(5)` and `range(1, 5)`?

**Answer:** `range(5)` generates numbers from 0 to 4, while `range(1, 5)` generates numbers from 1 to 4.

**Real-world example:** Counting from zero or starting a student count from one.

### Q5. What is the purpose of the `step` parameter in `range()`?

**Answer:** The `step` parameter determines the interval between generated numbers.

**Real-world example:** Counting every second item in a list.

### Q6. What is the difference between `enumerate()` and `zip()`?

**Answer:** `enumerate()` provides an index and value, while `zip()` combines corresponding items from multiple iterables.

**Real-world example:** Numbering students versus matching student names with marks.

### Q7. What happens if two lists passed to `zip()` have different lengths?

**Answer:** By default, `zip()` stops when the shortest iterable ends.

**Real-world example:** Matching names and marks when some students' marks are missing.

### Q8. What is the difference between an iterable and an iterator?

**Answer:** An iterable can provide an iterator, while an iterator returns values one at a time.

**Real-world example:** A playlist is iterable, and its playback mechanism can provide songs one by one.

### Q9. What is the difference between `iter()` and `next()`?

**Answer:** `iter()` creates an iterator, while `next()` retrieves its next value.

**Real-world example:** Preparing a playlist for playback and moving to the next song.

### Q10. What is `StopIteration`?

**Answer:** It is an exception raised when an iterator has no more values.

**Real-world example:** Reaching the end of a playlist.

### Q11. How does a `for` loop work internally?

**Answer:** A `for` loop obtains an iterator and retrieves values until the iterator is exhausted.

**Real-world example:** Reading student names one by one from a list.

### Q12. What is an infinite loop?

**Answer:** An infinite loop continues indefinitely because its stopping condition is never reached.

**Real-world example:** A monitoring program that continuously checks for updates.

### Q13. How can you prevent an infinite loop?

**Answer:** Ensure the loop condition eventually becomes `False` or provide a suitable stopping condition.

**Real-world example:** Ending a countdown when it reaches zero.

### Q14. Can we use `break` inside nested loops?

**Answer:** Yes. `break` terminates the innermost loop in which it is used.

**Real-world example:** Stopping a search within one classroom without automatically stopping the search through every classroom.

### Q15. Why is `enumerate()` preferred over manually maintaining an index?

**Answer:** `enumerate()` makes code simpler and reduces manual index-management errors.

**Real-world example:** Displaying numbered items in a shopping list.
