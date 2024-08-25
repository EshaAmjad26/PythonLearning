name2 = "Esha"
print(name2)              #DATA TYPES:
# data types              #1.premetive data types= store single value   e.g, int, float etc
#     string: str         #2.non-premetive data types= store multiple values in one variable e.g, list, tuple, dic etc
#     Integer: int
#     Float: float        #phases of variable: 1.Declaration, 2.Initialization
#     Boolean: bool.

Name1 : str = "Doctor's advice"
age : int = 22
height : float= 5
status : bool = False
print("My name is", Name1, "\nMy age is", age, "\nMy height is",height, "\nMy status is", status )

# convert word or string to title format (first letter always upper)
title1= "python learning "
print(title1.title())          #build-in methods depend on data types

#formatting string method, f method
firstName= "Esha"
LastName= "Amjad"
fullName= f"My full name is {firstName} {LastName}"
print(fullName)
#alternate and difficult method of 'f method'
print("I am {0} years old".format(age))
#rstrip and lstrip
language= "python      "
print(language.rstrip(),".") # rstrip remove white spaces from right side while lstrip remove white spaces from left side

 #Using %s and %d
# You can use %s for string and %d for integers.
name: str = "Alice"
AGE: int = 30
print("My name is %s and I am %d years old." % (name, AGE))

# Using .format()
# The .format() method is another way to format your strings.
x: int = 10
y: int = 20
print(f"The sum of {x} and {y} is {x+y}.")
#You can format numbers using f-strings.
pi: float = 3.14159
print(f"Value of pi to 2 decimal places: {pi:.2f}")
# Constants
# Use UPPER_SNAKE_CASE for constants.
PI: float = 3.14159
