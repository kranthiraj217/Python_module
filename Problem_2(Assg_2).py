#Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

d = {}
string = "abcdefghijklmonpqrstuvwxyz"
for each_char in string:
    d[each_char] = ord(each_char)
print(d)
