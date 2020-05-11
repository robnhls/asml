#!/usr/bin/etc python

"""
This is a Doc String
It will typicall describe the usage of a module
or a function.

Python is aware of Doc Strings and will display them in the help
"""

name = "rob"
print("Hello " + name)

age = 47
height = 5.8

# Strongly Typed Language
print(name + " is " + str(age)) # this will be a problem

file_name = r"c:\test\new_files\batch.py"


# single quoted strings
string1 = "this 'is' a string"
string2 = 'this is "also" a string'

# Triple quoted
string3 = '''This is a tripple quoted stiring'''
string4 = """ This 
si 
also 
a 
triple 
quoted string """

print(string4)


sample = "standard string"
print("regular sample:", sample)
print("upper method:", sample.upper())
print("regular sample again:", sample)

# this does not do what you think it does
print("count problem", sample.count("s"))
print("character count:", len(sample))

city = "Monroe"
population = 12000

# The population of ... is ...
message = "The population of {} is {}".format(city, population)
print(message)

message = "The population of {} is {:,}".format(city, population)
print(message)

# f strings 3.6+
message = f"The population of {city} is {population}"
print(message)
