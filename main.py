student_grade={
    'Pranjal':90,
    'Bob':50,
    "Manish":30
}
print(student_grade.values())
print(student_grade.items())
print(student_grade['Pranjal'])
print(student_grade['Bob'])
for student in student_grade:
    print(student, "scored",student_grade[student])

for student,grade in student_grade.items():
    print(student,grade)

message="This much for today!"
for char in message:
    print(char)