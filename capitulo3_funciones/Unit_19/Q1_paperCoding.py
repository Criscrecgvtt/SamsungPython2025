n_list = [1,2,3,4,5,6,7,8,9,10]

even_list = []

for a in filter((lambda x: x%2==0),n_list):
    even_list.append(a)
    
print(even_list)