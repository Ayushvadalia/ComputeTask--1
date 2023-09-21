n=input("Enter number of students")
n=int(n)
z=input("Enter number of subjects")
z=int(z)
student = {}


for i in range(n):
     name = input("Enter students name: ")
     for j in range(z):
        marks = input("Marks of students: ")
        student[name] = marks