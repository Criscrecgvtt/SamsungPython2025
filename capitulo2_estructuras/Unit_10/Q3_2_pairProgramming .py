s_list = ["bcdbc","abc","bcd","bcdefg","abba","cddc","opq"]
s_list.sort(key=len)
print(s_list)
aux = []
for i in s_list:
    size = len(i)
    if size == len(s_list[0]):
        aux.append(i)
    else:
        break
        
print(aux)