#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sample_list.sort(key = lambda r : r[-1])

print(sample_list)
