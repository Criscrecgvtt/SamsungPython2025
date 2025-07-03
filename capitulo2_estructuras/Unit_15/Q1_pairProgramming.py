student_tup = (('211101', 'David Doe', '010-1234-4500'),
               ('211102', ' John Smith', '010-2230-6540'),
               ('211103', ' Jane Carter', '010-3232-7788'))

res_dict = {s[0]: [s[1].strip(), s[2]] for s in student_tup}

for key , value in res_dict.items():
    print(key,":",value[0])

sid = input("Enter student ID number: ")
if sid in res_dict:
   student_car = res_dict.get(sid)
   print("Name:",student_car[0])
   print("Phone Number:",student_car[1])
else: 
    print("The student does not exist")