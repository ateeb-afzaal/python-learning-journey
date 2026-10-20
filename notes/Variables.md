Python Variables

Variables

- Variables are containers for storing data values.

Creating Variables

- Python has no command for creating variables.
- The variable is created the moment you first assign value to it.

  eg.
  x = 5
  y = 3.5
  print (x)
  print (y)

- Variables donot need to be declared with anytype and can change type after they have been set.
  eg.
  x = 5
  x= "Hello"
  print(x)

Casting

- If you want to specify a data type to a variable. You can done it by casting.

x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0

Get the Type

- You can get the type of variable with type() function.
  x = 5
  y = "Hello"

  print(type(x))
  print(type(y))

Single or Double Quotes?

- String variable can be declared by (') or (")
- x = 'Hello' and x = "Hello" are same.

Case-Sensitive

- Python is a case sensitive language
- x = 5 is different from X = 5.

Variable Names

- A variable ca have a short name like "x" or and more defining name lke "age"
  x = 5
  age = 23

RUles for declaring variable

- A variable can be start with a letter or number.
- Python is case sensitive so 'any' is different from 'ANY' and 'Any'.
- It can only include alpha-numeric characters and underscores (a-z, 0-9, \_).
- It cannot start with a number.
- A variable name canot e a python keyword (e.g if, else, delete, insert).

Multi Words Variable Names

- variable name with more than one word can be difficult to read (e.g myariablename).
- So we use different methods to make it easy.
  1. camel case
     Each word, except the first, starts with a capital letter: (e.g: myVariableName).

  2. Pascal case
     Each word starts with a capital letter: (e.g: MyVariableName).

  3. Snake Case
     Each word is seperated by a underscore: (e.g: my_variable_name).

Python Variables - Assign Multiple Values

Many Values to Multiple Variables

- Python allows you to assign values to multiple variables in one line:
  eg.
  x, y, z = "apple", "Banana", "Oange"

One Value to Multiple Variables

- You can assign one value to multiple variables.
  x = y = z = 5

Unpack a Collection

- If you have multiple values list or tuple you can extract them in variables, it is called unpakcking.
  eg.
  fruits = ["Apple", "Banana", "Orange"]
  x, y, z = fruits

Output Variables

- print() function is often used to output variables
  eg.

  x=5
  print(x)

- you an also output multiple varibles in single line with 1 print() function using ',' o seperate them.
  x=5
  y="Hello"
  z=2.6
  print(x, y, z)

- You can also use the + operator to output multiple variables:
  x = "How "
  y = "are "
  z = "You"
  print(x + y + z)

- For numbers, the + character works as a mathematical operator:
  x = 5
  y = 10
  print(x + y)

- In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

  x = 5
  y = "John"
  print(x + y)

- The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

  x = 5
  y = "John"
  print(x, y)

Global Variables

- variables that are created outside of a function are called global variables. These can be accessed inside and outside of function.

x = 5

def thisfunc():
print(5 + x)

thisfunc()

- If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

  x = "awesome"

  def myfunc():
  x = "fantastic"
  print("You are " + x)

  myfunc()

  print("You are" + x)

The global Keyword

- Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

- To create a global variable inside a function, you can use the global keyword.

  def myfunc():
  global x
  x = "fantastic"
  print("You are " + x)

  myfunc()

  print("You are " + x)

- You can change the value of global variable that you declared outside of function by using global inside the function.

  x = 10

  def myfunc():
  global x
  x = 20

  myfunc()

  print(x)
