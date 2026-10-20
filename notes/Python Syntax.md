Python Statements.

- A program is a set of excecuteable lines and these lines are called statemnts. Some coomon type of statemenst are
  1. Assigment statements (X = 5).
  2. Conditonal Statements (if, else).
  3. Loop statements (for, while).
     e.g print("Hello, There!")

- There can be multiple statements in a program.

  print("Hello")
  print("How are you")
  print("How was your day?")

  These lines will be executes one by one in sequential order.

- You can write multiple statements in a single line with the help of seperator ";".

  print("Hello"); print("How are you"); print("How was your day?")
  If you don't use semicolon you will get an Syntax error.

Python "print()" Function.

- You can use the print() function as many times as you want. Each call prints text on a new line by default:

  Example
  print("Hello World!")
  print("I am learning Python.")
  print("It is awesome!")

Double Quotes

- Text in python must be in single quotes (') or double quotes (").
- Example
  print("This will work!")
  print('This will also work!')

- If you forget to put the text inside quotes, Python will give an error:

  Example
  print(This will cause an error)

  Result:
  SyntaxError: invalid syntax.

Print Without a New Line

- normally the print function end with a new line but if you want to print multiple words on the same line you can use "end" parameter.

  print("Hello", end=" ")
  print("there")

Print Numbers

- You can also use print() function to print numbers.
  print(3)
  print(43)
  print(343)

- You can also do math inside print() function.
  print(3 + 3)
  print(4 / 2)

Mix Text and Numbers

- You can also print text and number in a single prnt() function.
  print("I am", 35, "years old.")

Python Comments

- It is used to explain python code.
- Comments can be used to make the program more readble.
- It can e used to prvent execution at the time of testing.

Creating a Comment

- Comments starts with a '#' Python ignores it.
  #this is a comment.

- Comments can be placed at the end of a line, and Python will ignore the rest of the line:
  print("Hello, World!") #This is a comment

- A comment can also be a code line
  #print("Hello, World!")

- There can also e multiple line comments.
  #comment 1.
  #comment 2.
  #comment 3.

OR

"""
This is a comment
Written in
More than 1 lines.
"""
