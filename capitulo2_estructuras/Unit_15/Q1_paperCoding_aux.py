student_tup = (('211101', 'David Doe', '010-1234-4500'),
               ('211102', ' John Smith', '010-2230-6540'),
               ('211103', ' Jane Carter', '010-3232-7788'))

res_dict = {}

for student in student_tup:
    student_id = student[0]
    name = student[1].strip()
    phone = student[2]
    res_dict[student_id] = [name, phone]

print(res_dict)
