# Python Lists

## 1. Introduction

A list is used to store multiple items in one variable.

Example:

    fruits = ["apple", "banana", "cherry"]

### List Properties

- Ordered: Items have a fixed order.
- Changeable: Items can be modified.
- Allows duplicates: The same value can appear multiple times.
- Different data types can be stored together.
- Lists are written using square brackets [].

---

## 2. Access List Items

Python list indexing starts from 0.

    fruits[0]   # First item
    fruits[1]   # Second item
    fruits[-1]  # Last item

### Negative Indexing

Negative indexes start counting from the end.

- -1 means the last item.
- -2 means the second-last item.

---

## 3. List Slicing

Syntax:

    list[start:end]

The start index is included.
The end index is excluded.

Examples:

    fruits[1:3]
    fruits[:3]
    fruits[2:]
    fruits[-3:-1]

---

## 4. Change List Items

Lists are changeable.

    fruits[1] = "orange"

Change multiple items:

    fruits[1:3] = ["kiwi", "mango"]

The number of replacement items can be different
from the number of selected items.

---

## 5. Add List Items

### append()

Adds one item at the end.

    fruits.append("mango")

### insert()

Adds an item at a specific index.

    fruits.insert(1, "orange")

### extend()

Adds multiple items from an iterable.

    fruits.extend(["kiwi", "grapes"])

Important:

append(["kiwi", "grapes"]) adds one nested list.

extend(["kiwi", "grapes"]) adds two separate items.

---

## 6. Remove List Items

### remove()

Removes the first matching item.

    fruits.remove("banana")

### pop()

Removes an item by index and returns it.

    fruits.pop(1)

Without an index, pop() removes the last item.

### del

Deletes an item or an entire list.

    del fruits[0]

### clear()

Removes all items but keeps the empty list.

    fruits.clear()

---

## 7. Loop Through Lists

### For Loop

    for x in fruits:
        print(x)

### While Loop

    i = 0

    while i < len(fruits):
        print(fruits[i])
        i += 1

Important:

Use < instead of <= to avoid an IndexError.

---

## 8. List Comprehension

List comprehension creates a new list
using a shorter syntax.

Syntax:

    newlist = [expression for item in iterable if condition]

Example:

    newlist = [x for x in fruits if "a" in x]

### With If-Else

    newlist = [x if x == "banana" else "orange" for x in fruits]

If the condition is True, use x.
Otherwise, use "orange".

---

## 9. Sort Lists

### Ascending Order

    numbers.sort()

### Descending Order

    numbers.sort(reverse=True)

### Alphabetical Order

    fruits.sort()

### Custom Sorting

    def myfunc(n):
        return abs(n - 50)

    numbers.sort(key=myfunc)

The key function determines the sorting order.

---

## 10. Copy Lists

### copy()

    newlist = fruits.copy()

Creates a separate shallow copy.

### list()

    newlist = list(fruits)

Also creates a shallow copy.

Important:

    newlist = fruits

This does not create a separate list.
Both variables reference the same list.

---

## 11. Join Lists

### Using +

    list3 = list1 + list2

### Using extend()

    list1.extend(list2)

### Using a For Loop

    for x in list2:
        list1.append(x)

---

## 12. Useful List Methods

| Method    | Description                |
| --------- | -------------------------- |
| append()  | Add one item at the end    |
| extend()  | Add items from an iterable |
| insert()  | Insert an item at an index |
| remove()  | Remove first matching item |
| pop()     | Remove and return an item  |
| clear()   | Remove all items           |
| copy()    | Create a shallow copy      |
| count()   | Count occurrences          |
| index()   | Find first matching index  |
| sort()    | Sort items                 |
| reverse() | Reverse item order         |

---

## 13. Useful Built-in Functions

| Function | Description              |
| -------- | ------------------------ |
| len()    | Number of items          |
| max()    | Largest item             |
| min()    | Smallest item            |
| sum()    | Sum of numeric items     |
| sorted() | Return a new sorted list |

---

## 14. Important Points

1. List indexes start at 0.
2. Negative indexes count from the end.
3. Slicing excludes the ending index.
4. Lists allow duplicate values.
5. Lists can store different data types.
6. append() adds one item.
7. extend() adds multiple items.
8. remove() deletes the first matching value.
9. sort() changes the original list.
10. copy() creates a separate shallow copy.

---

## 15. Practice Completed

Project: Fruit Shop Inventory

Topics practised:

- Indexing and slicing
- Adding and removing items
- For loops
- List comprehension
- Sorting
- Copying
- Counting duplicate items

Coding Assessment: 11/11
Quiz Score: 8/10

Learning Resource:
https://www.w3schools.com/python/python_lists.asp
