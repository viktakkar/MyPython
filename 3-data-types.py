"""Python’s Data Types #
Unlike many other languages, Python does not place a strong emphasis on defining the data type of an object, 
which makes coding much simpler. We’ll learn more about this in the near future.

The language provides three main data types:

1. Numbers
2. Strings
3. Booleans

Naming Conventions:
-- There are certain rules we have to follow when picking the name for a variable:
-- The name can start with an upper or lower case alphabet.
-- A number can appear in the name, but not at the beginning.
-- The _ character can appear anywhere in the name.
-- Spaces are not allowed. Instead, we must use snake_case to make variable names readable.
-- The name of the variable should be something meaningful that describes the value it holds, instead of being random characters.

"""

# ------------ INTEGER VARIABLES ------------
var_integer = 123456789  # Assigning an integer to a variable
print("Variable num = ",var_integer)

var_minus_integer = -16000  # Assigning a new integer
print("Assigning a minus number = ",var_minus_integer)

# ------------ FLOAT VARIABLES ------------
var_flt_positive=1.00000000005
print(var_flt_positive)  # A positive float

var_flt_negative=-85.6701
print(var_flt_negative)  # A negative float

flt_pt = 1.23456789
print(flt_pt)

# --------- Boolean ----------------
var_boolean = False
print(var_boolean)

# --------- String  ----------------
print('String')
print("Harry Potter!")  # Double quotation marks

got = 'Game of Thrones...'  # Single quotation marks
print(got)
print("$")  # Single character

# len length function
empty = ""
print(len(empty))
print(len(got))

# ------------- Indexing =-----------------
print('Indexing')
batman = "Bruce Wayne"

first = batman[0]  # Accessing the first character
print(first)

space = batman[5]  # Accessing the empty space in the string
print(space)

last = batman[len(batman)-1]
print(last)
# The following will produce an error since the index is out of bounds
# err = batman[len(batman)]

# ------------- Reverse Indexing -----------------
print('Reverse Indexing')
batman = "Bruce Wayne"
print(batman[-1])  # Corresponds to batman[10]
print(batman[-5])  # Corresponds to batman[6]