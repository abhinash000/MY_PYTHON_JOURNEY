# Google Certification
# spam_amount is initialized to 0
# This program demonstrates various data types in Python.

# Integer Data Type: Represents whole numbers.
integer_value = 10
print("Integer:", integer_value)

# Float Data Type: Represents decimal numbers.
float_value = 10.5
print("Float:", float_value)

# String Data Type: Represents a sequence of characters.
string_value = "Hello, World!"
print("String:", string_value)

# Boolean Data Type: Represents True or False values.
boolean_value = True
print("Boolean:", boolean_value)

# List Data Type: Represents an ordered collection of items.
list_value = [1, 2, 3, 4, 5]
print("List:", list_value)

# Tuple Data Type: Represents an immutable ordered collection of items.
tuple_value = (1, 2, 3)
print("Tuple:", tuple_value)

# Dictionary Data Type: Represents key-value pairs.
dict_value = {"name": "John", "age": 30}
print("Dictionary:", dict_value)

# Set Data Type: Represents an unordered collection of unique items.
set_value = {1, 2, 3, 4, 5}
print("Set:", set_value)

# None Data Type: Represents the absence of a value or a null value.
none_value = None
print("None:", none_value)
#_____________________________________________________________________________________________________________
spam_amount = 0
print(spam_amount)

# Increment spam_amount by 4
spam_amount = spam_amount + 4

# Check if spam_amount is greater than 0
if spam_amount > 0:
    print("but I don't want any spam")

# Assign a string to viking_song and print it
viking_song = "spam spam spam spam"
print(viking_song)

# ____________________________________________________________________________________________________________________________
# Arithmetic Operators

a = 8  # Assign value to variable a
b = 4  # Assign value to variable b
c = 2  # Assign value to variable c

# Perform arithmetic operations
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a / c)  # True division (division resulting in a float)
print(a // b)  # Floor division (integer division result)
print(a % b)  # Modulus operator (remainder of division)
print(a ** b)  # Exponentiation (a raised to the power b)

# ------------------------------------------------------------------------------------------------------------------
# Even or Odd Number Program

a = int(input())  # Take user input and convert it to an integer
if a % 2 == 1:  # Check if the number is odd
    print("odd")
else:
    print("even")

# -------------------------------------------------------------------------------------------------------
# Proving that except 0, all numbers (-∞, -1) ∪ (1, ∞) are considered true in Python.

if -1:  # -1 is considered True
    print("odd")
else:
    print("even")

# --------------------------------------------------------------------------------------------------------------
# Relational Operators
# ____________________________________________
# Compare two inputs
"""Operator 	Name 	             Example 	
== 	          Equal 	             x == y 	
!= 	          Not equal 	         x != y 	
>          	Greater than             x > y 	
< 	          Less than 	         x < y 	
>=    	Greater than or equal to 	x >= y 	
<= 	    Less than or equal to       x <= y
_____________________________________________"""


a = input()  # Take first input
b = input()  # Take second input

# Compare the two inputs
if a > b:
    print("big")
elif a < b:
    print(" a is smaller")
elif a == b:
    print("equal")
elif a >= b:
    print(" a is greater than of equal b ")    
elif a<=b:
    print(" a is less than of eaqal to b")
else:
    print(" no brain")

"""BITWISE OPERATORS
--------------------------------------------------------------
Python Bitwise Operators

Bitwise operators are used to compare (binary) numbers:
Operator 	Name 	Description 	                                 Example 	
&   	    AND 	Sets each bit to 1 if both bits are 1 	        | x & y 	
|   	    OR  	Sets each bit to 1 if one of two bits is 1      | x | y 	
^ 	        XOR     Sets each bit to 1 if only one of two bits is 1 | x ^ y 	
~   	    NOT     Inverts all the bits 	~x 	
<< 	        Zero    fill left shift 	Shift left by pushing zeros in from the right and let the leftmost bits fall off 	x << 2 	
>> 	        Signed  right shift 	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off 	x >> 2"""
 
#-----------------------------------------------------------------------------------------------------------------------
z=5
y=3
print(z&y)
"""Each bit of z and y is compared:

    0 & 0 = 0
    1 & 1 = 1
    0 & 1 = 0
    1 & 1 = 1
    Final binary result: 0001."""

print(z|y)
"""
Each bit of z and y is compared:
0 | 0 = 0
1 | 1 = 1
0 | 1 = 1
1 | 1 = 1
Final binary result: 0111."""
print(z^y)
"""
0 ^ 0 = 0
1 ^ 1 = 0
0 ^ 1 = 1
1 ^ 0 = 1
Final binary result: 0110.
    """
print(~y)
"""reverse all 0 to 1 and  1 to 0"""
    
print(z<<2)
# 0101 → 10100.
print(z>>3)
#hifting right by 2 places:
#0101 → 0001
 
 