score = int(input('Enter score : '))
if score >= 90:         # If 90 or above, 'A'
    grade = 'A'
elif score >= 80:       # If not 'A', 'B' if 80 or above
    grade = 'B'
elif score >= 70:       # If not 'B', 'C' if 70 or above
    grade = 'C'
elif score >= 60:       # If not 'C', 'D' if 60 or above
    grade = 'D'
else:                   # Otherwise, 'F'
    grade = 'F'
print('Your grade is: ', grade)
