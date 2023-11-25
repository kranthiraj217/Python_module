#Write a Python program to reverse a string.

def reverse_string(s):
    reversed_s = ""
    for i in range(len(s)-1,-1,-1):
        print(f"At postion : {i}, the element is : {s[i]}")
        reversed_s += s[i]
    return reversed_s

string = "entertainment"
reverse_string(string)
