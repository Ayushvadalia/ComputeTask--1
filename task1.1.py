

x = int(3)
stud1 = [100]
stud2 = [100]
stud3 = [100]
n = int(3)

print("Enter marks of subject 1")
for i in range(0, n):
    ele = int(input())
    stud1.append(ele)

print("Enter marks of subject 2")
for i in range(0, n):
    ele = int(input())
    stud2.append(ele)

print("Enter marks of subject 3")
for i in range(0, n):
    ele = int(input())
    stud3.append(ele)

print("Average marks of student 1")
print((stud1[1] + stud1[2] + stud1[3]) / 3)
print("Average marks of student 2")
print((stud2[1] + stud2[2] + stud2[3]) / 3)
print("Average marks of student 3")
print((stud3[1] + stud3[2] + stud3[3]) / 3)


