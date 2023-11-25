 #Write a Python function to sum all the numbers in a list.
 
 def list_sum(l):
    sum_of_list_elements = 0
    for i in range(len(l)):
        sum_of_list_elements += l[i]
        print(f"At position : {i} the element is : {l[i]}")
    return sum_of_list_elements

sample_list = [5,2,7,11,6,9,13]
result = list_sum(sample_list)
print("result_of_list : ",result)  
