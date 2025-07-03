student_tup = (('211101', 'David Doe', '010-1234-4500'),
               ('211102', ' John Smith', '010-2230-6540'),
               ('211103', ' Jane Carter', '010-3232-7788'))

res_dict ={}
for i in range(len(student_tup)):
    list = []
    for j in range(len(student_tup[i])):
        if j==0:
            res_dict[student_tup[i][j]] = list
        else:
            list_aux =  res_dict[student_tup[i][0]]
            list_aux.append(student_tup[i][j])
            res_dict[student_tup[i][0]] = list_aux

print(res_dict)