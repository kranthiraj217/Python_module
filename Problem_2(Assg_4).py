l = input("Enter the elements of list seperated by spaces : ").split()
user_list = list(map(int, l))
tripled = list(map(lambda x : x * 3, user_list))
print(tripled)
