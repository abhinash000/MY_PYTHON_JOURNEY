# The first program: Hello World!
#Python is a programming language invented by Guido van Rossum in the late 1980s. It's like a tool that helps computers understand and follow instructions.

#Here's a simple timeline:

#1991: Python was first released. 
#Over the years: It has grown bigger and smarter, learning to do more things.
#Today: Python is very popular because it's easy to learn and use. People use it for many things, like making websites, analyzing data, and even building robots!
#

print("Hello world!")  # This line prints the message "Hello world!"

# Part 2: Variables in Python

# Variables store data and can be used later in your program.

x = 3             # Integer (whole number)
y = 4.0           # Float (decimal number)
A = "Abhi, I am programmmer"  # String (text)

# Multiple variable assignment in one line:
p, i, z = "Pipe", "Pepsi", "Mazaa"

# Printing variable values:
print(x)
print(y)
print(A)

# Checking variable data types:
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(A))  # Output: <class 'str'>

# The data types in python programming
B = 143         # Integer (whole number)
C = 14.3        # Float (decimal number)
D = 1j          # Complex number (imaginary unit)
E = ["i", "am", "hacker", "baby"]  # List (ordered collection of items)
F = ("god", "must", "crazy")  # Tuple (immutable ordered collection)
G = range(6)  # Range (sequence of numbers)
# Caution: Lists are mutable, tuples are immutable. Choose wisely.
h = {"name": "bhasha", "age": 47}  # Dictionary (key-value pairs)
I = frozenset({"apple", "and", "newton"})  # Frozen set (immutable collection)
j = True  # Boolean (True or False)
print(A, B, C, D, E, F, G, h, I, j)

#for showing their data types
# \t for giving the space between variables  and their  values 
print("Variable\tValue\tData Type")

print("A\t", A, "\t", type(A))

print("B\t", B, "\t", type(B))

print("C\t", C, "\t", type(C))

print("D\t", D, "\t", type(D))

print("E\t", E, "\t", type(E))

print("F\t", F, "\t", type(F))

print("G\t", G, "\t", type(G))

print("h\t", h, "\t", type(h))

print("I\t", I, "\t", type(I))

print("j\t", j, "\t", type(j))