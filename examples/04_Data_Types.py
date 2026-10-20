# Data Types


x = "Hello"
print(x)
print(type(x)) 

x = 20
print(x)
print(type(x)) 

x = 20.0
print(x)
print(type(x)) 

x = 1j
print(x)
print(type(x)) 

x = ["apple", "Banana"]
print(x)
print(type(x)) 

x = ("apple", "Banana")
print(x)
print(type(x)) 

x = range(6)
print(x)
print(type(x)) 

x = {"apple" : "Banana"}
print(x)
print(type(x)) 

x = True
print(x)
print(type(x)) 

x = {"apple", "Banana"}
print(x)
print(type(x)) 

x = frozenset({"apple", "Banana"})
print(x) 
print(type(x))

x = b"Hello"
print(x)
print(type(x))

x = bytearray(5)
print(x)
print(type(x))

x = memoryview(bytes(5))
print(x)
print(type(x)) 

x = None
print(x)
print(type(x)) 

# Expected output
# Hello
# <class 'str'>
# 20
# <class 'int'>
# 20.0
# <class 'float'>
# 1j
# <class 'complex'>
# ['apple', 'Banana']
# <class 'list'>
# ('apple', 'Banana')
# <class 'tuple'>
# range(0, 6)
# <class 'range'>
# {'apple': 'Banana'}
# <class 'dict'>
# True
# <class 'bool'>
# {'apple', 'Banana'}
# <class 'set'>
# frozenset({'apple', 'Banana'})
# <class 'frozenset'>
# b'Hello'
# <class 'bytes'>
# bytearray(b'\x00\x00\x00\x00\x00')
# <class 'bytearray'>
# <memory at 0x7f8c1c2e4d00>
# <class 'memoryview'>
# None
# <class 'NoneType'>


# Type Conversion

x = float(5)
y = int(5.9)
z = complex(20)


print(x)
print(y)
print(z)


print(type(x))
print(type(y))
print(type(z))

# Expected output
# 5.0   
# 5
# (20+0j)
# <class 'float'>
# <class 'int'>
# <class 'complex'>

# random module
import random

print (random.randrange(0, 10))

# Expected output
# A random number between 0 and 10 (excluding 10)

# lenght of a string
a = "banana"

print(len(a))

# Expected output
# 6


# Check String

a = "banana"
print("ana" in a)

# Expected output
# True

# checking with if statement
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Expected output
# Yes, 'free' is present.


# Slicing Strings

b = "Hello, World!"
print(b[2:5])

# Expected output
# llo


#conatenation of strings

a = "Hello"
b = "World"
c = a + b
print(c)

# Expected output
# HelloWorld

a = "Hello"
b = "World" 
print(a + " " + b)

# Expected output
# Hello World


