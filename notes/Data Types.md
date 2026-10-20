Python Data Types

- Data types are important in every programming language.
- Variables can store data of different types, and different types can do different things.
- Python has build in data types.

Text: str
Numeric: int, float, complex
Seqence: list, tuple, range
mapping: dict
set: set, frozenset
boolean: bool
binary: bytes, bytearray, memoryview
none: NoneType

Python Numbers

- There are three numeric types in Python:

1. int
2. float
3. complex

- Variables of numeric types are created when you assign a value to them:

Example

x = 1 # int
y = 2.8 # float
z = 1j # complex

- To verify the type of any object in Python, use the type() function:

Example
print(type(x))
print(type(y))
print(type(z))

Int

- Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

Example
Integers:

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

Float

- Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

Example
Floats:

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

- Float can also be scientific numbers with an "e" to indicate the power of 10.

Example
Floats:

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

Complex

- Complex numbers are written with a "j" as the imaginary part:

Example
Complex:

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

Type Conversion

- You can convert from one type to another with the int(), float(), and complex() methods:

Example
Convert from one type to another:

x = 1 # int
y = 2.8 # float
z = 1j # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

Note: You cannot convert complex numbers into another number type.

Random Number

- Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

Example
Import the random module, and display a random number from 1 to 9:

import random

print(random.randrange(1, 10))

Python Casting

- There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

- int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
- float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
- str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

Python Strings

- Strings in python are surrounded by either single quotation marks, or double quotation marks.

- 'hello' is the same as "hello".

- You can display a string literal with the print() function:

Example
print("Hello")
print('Hello')

Quotes Inside Quotes

- You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

Example
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

Assign String to a Variable

- Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

Example
a = "Hello"
print(a)

Multiline Strings

- You can assign a multiline string to a variable by using three quotes:

Example
You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

Strings are Arrays

- Like many other popular programming languages, strings in Python are arrays of unicode characters.

- However, Python does not have a character data type, a single character is simply a string with a length of 1.

- Square brackets can be used to access elements of the string.

Example

- Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])

Looping Through a String

- Since strings are arrays, we can loop through the characters in a string, with a for loop.

Example

- Loop through the letters in the word "banana":

for x in "banana":
print(x)

String Length

- To get the length of a string, use the len() function.

Example

- The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))

Check String

- To check if a certain phrase or character is present in a string, we can use the keyword in.

Example

- Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)

- Use it in an if statement:

Example
Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
print("Yes, 'free' is present.")

Python - Slicing Strings

Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

Example
Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])

Slice From the Start

- By leaving out the start index, the range will start at the first character:

Example
Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])

Slice To the End

- By leaving out the end index, the range will go to the end:

Example
Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])

Negative Indexing

- Use negative indexes to start the slice from the end of the string:
  Example
  Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])

Python - Modify Strings

Upper Case
Example

- The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())
Lower Case
Example

- The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())

Remove Whitespace
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

Example

- The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

Replace String

Example

- The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))

String Concatenation

- To concatenate, or combine, two strings you can use the + operator.

ExampleGet your own Python Server

- Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)

- To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)

Python - Format - Strings

String Format

- As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

Example
age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)

F-Strings

- F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

- To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

Example
Create an f-string:

age = 36
txt = f"My name is John, I am {age}"
print(txt)

Placeholders and Modifiers

- A placeholder can contain variables, operations, functions, and modifiers to format the value.

Example
Add a placeholder for the price variable:

price = 59
txt = f"The price is {price} dollars"
print(txt)
A placeholder can include a modifier to format the value.

- A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

Example
Display the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

Escape Character

- To insert characters that are illegal in a string, use an escape character.

- An escape character is a backslash \ followed by the character you want to insert.

- An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

Example
You will get an error if you use double quotes inside a string that is surrounded by double quotes:

txt = "We are the so-called "Vikings" from the north."
To fix this problem, use the escape character \":

Example
The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."
