name = ("Aashiya","Firoz","Khan","Jaju")
scores = (30,60,80,90)

def func_1():
  students = []
  for i in range(len(name)):
    students.append([name[i],scores[i]])
  print(students)
  for i in students:
   if i[1] > 70:
    print(i)
func_1()