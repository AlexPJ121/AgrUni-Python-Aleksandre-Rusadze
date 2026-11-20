choice=input('Enter the name of the student: ')
subjects={'math':{'George':85,'Salome':78,'David':92},
          'physics':{'George':90,'David':75,'Salome':88},
          'chemistry':{'David':82,'George':80,'Salome':91}}
student={}
for subject,grades in subjects.items():
  for name,score in grades.items():
    if name not in student:
      student[name]={}
    student[name][subject]=score
#print(student)
print(student[choice])

