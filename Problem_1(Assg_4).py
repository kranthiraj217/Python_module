#Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
n = int(input("enter the number : "))
add = (lambda num : num + 25)(n)
print("The sum after adding is : ", add)
