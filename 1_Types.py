import random

# *************************************************************
# String Types (str)
# *************************************************************
# str
string_1 = "This is a string"
string_join = string_1 + "that has been joined"
string_slice_single = string_join[0]  # Get first character (index 0)
string_slice_reverse = string_join[-1]  # Get the last character (index -1)
string_slice_range = string_join[0:4]  # Get characters from index 0 up to but not including index 4 "This"
string_slice_range_2 = string_join[2:-2]  # Get characters from index 2 up to but not including the last two characters
string_slice_range_3 = string_join[2:]  # Get characters from index 2 all the way to the end of the string
string_slice_range_4 = string_join[:5]  # Get characters first 5 characters
string_slice_range_5 = string_join[-2:]  # Get last two characters
string_index_a = string_join.index('a')  # Get index of the first 'a'
string_index_is = string_join.index('is')  # Get index of the first occurrence of 'is'
string_uppercase = string_join.upper()  # Transform string to all uppercase
string_lowercase = string_join.lower()  # Transform string to all lowercase
string_convert_float = str(4.23)  # Convert number to a string
string_length = len(string_1)  # Get length of string
# *************************************************************
# Numeric Types (int, float, complex, random)*****
# *************************************************************
# int
integer_1 = 7
integer_2 = -20
integer_convert_float = int(7.3)  # Convert float to integer (VALUE: 7) - NOTE: Python just drops the decimals (no rounding)
integer_convert_string = int("2")  # Convert string to integer (VALUE: 2)

# float
float_1 = 13.25
float_2 = -50.1
float_3 = 10e20  # exponential notation
float_convert_int = int(7)  # Convert integer to float (VALUE: 7.0)
float_convert_string = int("2.1")  # Convert string to float (VALUE: 2.1)

# complex
complex_1 = 7j  # Always postfix with a 'j'

# random - NOTE: There is no random type, you have to use the random module (imported)
random_1 = random.randrange(1, 100)  # Random number between 1 and 100 as an int

# *************************************************************
# Boolean Types (bool)
# *************************************************************
# bool
boolean_1 = True  # NOTE: Uppercase first letter!

# *************************************************************
# None Type (None)
# *************************************************************
# None
none_1 = None  # None type signifies that the variable has no value - this is different to empty string

# *************************************************************
# Sequence Types (list, tuple, range, dict)
# *************************************************************
# list - NOTE: Lists can mix the contained element types
list_1 = ["Windows", "MacOs", "Linux"]
list_length = len(list_1)  # Get count of elements (VALUE: 3)
list_1.append("Solaris")  # Add an element to the list
list_2 = list_1[0]  # Get first element
list_3 = list_1[1:3]  # Get second and third elements (returns a new list)
list_concat = list_1 + list_3  # Add two lists together
list_3 += list_1  # Add list_1 to list_3
list_val_1 = list_3.pop(3)  # Remove element at index 3 and returns to list_val
list_3[-1] = "Another Element"  # Replace the element at the last index in the list
list_3[0] = ["Dog", "Cat", "Fish"]  # Add a nested list into a list (multi-dimensional list)
list_val_2 = list_3[0][2]  # Get the third element from the nested list. The list from index 0 then val from index 2

# tuple
g = ("Windows", "MacOS", "Linux")

# range
h = range(10)  # This will create a range between 0 and 10. i.e. 11 elements

# dict - Dict is a key / value collection
i = {"name": "Jason", "age": 25}

# *************************************************************
# ***** Mapping Types (set, frozenset) *****
# *************************************************************
# set
j = {"MacOS", "Windows", "Linux"}
# frozenset
k = ({"MacOS", "Windows", "Linux"})

# *************************************************************
# ***** Binary Types (bytes, bytearray, memoryview) *****
# *************************************************************
# bytes
m = b"Hello"  # prefix with 'b'
# bytearray
n = bytearray(2)
# memoryview
o = memoryview(bytes(8))
