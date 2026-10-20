# Creating Variables
x = 5
y = 3.54
print(x)
print(y)

# Expected output
# 5
# 3.54

# Changing Variable types

x = 5 # x is of type int
x = "Hello" # x is of type str
print(x)

# Expected output
# Hello 

#Casting
x = int(5)
y = float(5)
z = str(5)

print(x)
print(y)
print(z)

# Expected output
# 5
# 5.0
# 5

# Get the Type

x = 5
y = "Hello"
print(type(x))
print(type(y))

# Expected output
# <class 'int'> 
# <class 'str'>

#Case Sensitivity
a = 4
A = "Hello"
print(a)
print(A)

# Expected output
# 4
# Hello

# Many Values to Multiple Variables
x, y, z = "Apple", "Banana", "Orange"

print(x)
print(y)
print(z)

# Expected output
# Apple
# Banana
# Orange

# One Value to Multiple Variables
x = y = z = 4
print(x)
print(y)
print(z)

# Expected output
# 4
# 4
# 4

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

# Expected output
# apple
# banana
# cherry

# Output Variables

x=5
y="Hello"
z=2.6

print(x, y, z)

# Expected output
# 5 Hello 2.6

x = "How "
y = "are "
z = "You"
print(x + y + z)

# Expected output
# How are You

x = 5
y = 10
print(x * y)

# Expected output
# 50


# Global Variables
x = 5

def thisfunc():
	print(5 + x)
   
thisfunc()

# Expected output
# 10


# Local and global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  print("You are " + x)
    
myfunc()

print("You are" + x)

# Expected output
# You are fantastic
# You are awesome

# Global Keyword

def myfunc():
  global x 
  x = "fantastic"
  print("You are " + x)
    
myfunc()

print("You are " + x)

# Expected output
# You are fantastic
# You are fantastic

# changing global variable inside a function

x = 10

def myfunc():
  global x
  x = 20
    
myfunc()

print(x)

# Expected output
# 20    