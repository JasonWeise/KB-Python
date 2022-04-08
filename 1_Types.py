import random

# *************************************************************
# String Types (str)
# *************************************************************
# str
s1 = "This is a string"

# *************************************************************
# ***** Numeric Types (int, float, complex, random)*****
# *************************************************************
# int
i1 = 7
i2 = -20
# float
f1 = 13.25
f2 = -50.1
f3 = 10e20  # exponential notation
# complex
c1 = 7j  # Always postfix with a 'j'
# random - NOTE: There is no random type, you have to use the random module (imported)
r1 = random.randrange(1, 100)  # Random number between 1 and 100 as an int

# CONVERSION
convert_f = float(i1)  # convert int to float - eg 7 = 7.0
convert_i = int(f1)  # convert float to int - eg 13.25 = 13 (note round up over .5 and round down .5 and under)
convert_c = complex(f1)  # convert to complex

# *************************************************************
# ***** Sequence Types (list, tuple, range, dict) *****
# *************************************************************
# list
f = ["Windows", "MacOs", "Linux"]
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
# ***** Boolean Types (bool) *****
# *************************************************************
# bool
l: bool = True  # NOTE: Uppercase first letter!

# *************************************************************
# ***** Binary Types (bytes, bytearray, memoryview) *****
# *************************************************************
# bytes
m = b"Hello"  # prefix with 'b'
# bytearray
n = bytearray(2)
# memoryview
o = memoryview(bytes(8))
