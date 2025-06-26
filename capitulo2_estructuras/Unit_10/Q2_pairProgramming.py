s_list = ["bcdbc","abc","bcd","bcdefg","abba","cddc","opq"]
max_elem = ""
for i in s_list:
    if len(i) > len(max_elem):
        max_elem = i

print("The longest string is",max_elem)