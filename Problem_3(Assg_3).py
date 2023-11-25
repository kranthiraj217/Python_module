#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.


import re

def count_upper_lower(s):
    count_lower = 0
    count_upper = 0
    for i in s:
        count_upper = len(re.findall(r'[A-Z]',string))
        count_lower = len(re.findall(r'[a-z]',string))
    return count_lower, count_upper

string = "The quick Brow Fox"
upper,lower = count_upper_lower(string)
print("Upper case Count : ", upper)
print("Lower case Count : ", lower)
        
