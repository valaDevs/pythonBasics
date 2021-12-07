# containers for stroing data
#A variable is created the moment you first assign a value to it.

name = "vala"
age = 22
married = False
grade = 1.6

x = float(2) #==> 2.0
y = str(3) #==> "3"
z = int(3)#==> 3

name2 = 'vala'





"""
    Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
"""


myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"





x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)




x = y = z = "Orange"
print(x)
print(y)
print(z)




print(name)
print(age)




def myfunc():
    global m
    m = "fantastic"

myfunc()

print("Python is " + m)