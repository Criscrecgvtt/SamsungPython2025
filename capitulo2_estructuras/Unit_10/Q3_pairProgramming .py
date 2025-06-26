s_list = ["bcdbc","abc","bcd","bcdefg","abba","cddc","opq"]
min_elem =[ s_list[0]]
for i in s_list:
    size = len(i)
    if size <len(min_elem[0]):
        min_elem = [i]
    elif size == len(min_elem[0]):
        min_elem.append(i)
        
print(min_elem)