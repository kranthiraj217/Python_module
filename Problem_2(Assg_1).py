#Write a Python program that accepts a word from the user and reverse it.
string = input()
index = len(string) - 1
rev_str = ""
while(index >= 0):
    rev_str = rev_str + string[index]
    index = index - 1    
print(rev_str)
