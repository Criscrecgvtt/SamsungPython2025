import copy
mylist = [(1, 2), (4, 5), (4, 2), (3, 1), (9, 4)]
aux_list = copy.deepcopy(mylist)
for tup in aux_list:
    tup = set(tup)
    
print(mylist)
a,b = input("Enter two numbers: ").split(" ")
a,b = int(a),int(b)
two_num = (a,b)




