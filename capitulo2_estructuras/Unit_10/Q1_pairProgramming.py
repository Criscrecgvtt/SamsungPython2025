s_list = ["bcdbc","abc","bcd","bcdefg","abba","cddc","opq"]
min_elem = s_list[0]
for i in s_list:
    if len(i) < len(min_elem):
        min_elem = i

print("The shorstes string is",min_elem)