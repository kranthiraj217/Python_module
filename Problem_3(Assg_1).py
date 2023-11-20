#Write a Python program to count the number of even and odd numbers from a series of numbers.
s = list(range(0,20))
count_even = 0
count_odd = 0
for i in range(len(s)+1):
    if i % 2 == 0:
        count_even = count_even + 1
    else:
        count_odd = count_odd + 1
print(s)
print(count_even, count_odd)
