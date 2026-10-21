

# My Python Lists program
# Topic: Python Lists
# Learning Resource: W3Schools

# A list stores multiple items in a single variable.
# Lists are ordered, changeable, and allow duplicate values.

# 1. Creating a list
fruits = ["apple", "banana", "cherry", "mango", "banana"]
print(fruits)

# 2. List length
# len() returns the total number of items.
print(len(fruits))

# 3. Accessing list items
# Indexing starts from 0.
print(fruits[0])   # First item
print(fruits[-1])  # Last item

# 4. List slicing
# The start index is included, but the end is excluded.
print(fruits[1:3])
print(fruits[:3])
print(fruits[2:])

# 5. Checking if an item exists
if "apple" in fruits:
    print("Apple is in the list")

# 6. Changing a list item
fruits[2] = "orange"
print(fruits)

# 7. Changing multiple items
fruits[1:3] = ["grapes", "watermelon"]
print(fruits)

# 8. Adding one item
# append() adds an item at the end.
fruits.append("kiwi")
print(fruits)

# 9. Adding an item at a specific position
fruits.insert(1, "peach")
print(fruits)

# 10. Adding multiple items
# extend() adds items from another iterable.
fruits.extend(["pineapple", "strawberry"])
print(fruits)

# 11. Removing an item
# remove() removes the first matching value.
fruits.remove("apple")
print(fruits)

# 12. Removing an item by index
# pop() removes and returns an item.
fruits.pop(0)
print(fruits)

# 13. Using a for loop
for x in fruits:
    print(x)

# 14. Using a while loop
i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1

# 15. List comprehension
# Create a new list containing fruits with the letter "a".
newlist = [x for x in fruits if "a" in x]
print(newlist)

# 16. List comprehension with if-else
# Replace every item except banana with orange.
newlist = [x if x == "banana" else "orange" for x in fruits]
print(newlist)

# 17. Sorting a list alphabetically
fruits.sort()
print(fruits)

# 18. Sorting in reverse order
fruits.sort(reverse=True)
print(fruits)

# 19. Sorting numbers
numbers = [100, 50, 65, 82, 23]
numbers.sort()
print(numbers)

# 20. Custom sorting
# Sort numbers based on their distance from 50.
def myfunc(n):
    return abs(n - 50)

numbers.sort(key=myfunc)
print(numbers)

# 21. Copying a list
# copy() creates a separate list.
copylist = fruits.copy()
print(copylist)

# 22. Joining lists
list1 = ["apple", "banana"]
list2 = ["cherry", "mango"]

joinedlist = list1 + list2
print(joinedlist)

# 23. Joining lists using extend()
list1.extend(list2)
print(list1)

# 24. Counting duplicate items
# Count how many times banana appears.
fruits = ["apple", "banana", "cherry", "banana", "mango", "banana"]

count = 0

for x in fruits:
    if x == "banana":
        count = count + 1

print(count)  # Expected output: 3

# 25. Using count()
print(fruits.count("banana"))  # Output: 3

# 26. Clearing a list
temp = ["apple", "banana", "cherry"]
temp.clear()
print(temp)  # Output: []

# 27. Deleting a list
temp = ["apple", "banana"]
del temp

# End of Python Lists examples
