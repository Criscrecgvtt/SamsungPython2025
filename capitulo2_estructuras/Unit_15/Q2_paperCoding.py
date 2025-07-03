student_tup = (('211101', 'David Doe', '010-1234-4500'),
               ('211102', ' John Smith', '010-2230-6540'),
               ('211103', ' Jane Carter', '010-3232-7788'))

student_dic = {}

for tupla in student_tup:
    student_dic[tupla[0]] = list(tupla[1:])

sid = input("Enter student ID number: ")
student_car = student_dic.get(sid, "none")
if (student_car != "none"):
    print("Name",student_car[0])
    print("Phone Number",student_car[1])
else:
    print("The student does not exist")