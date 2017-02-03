__author__ = 'Murtaza'
import re

def has_number_1(string):
    return any(char.isdigit() for char in string)

def has_number_2(string):
    return bool(re.search('\d',string))

# 2 is faster than 1
print has_number_2("Murtz1U")