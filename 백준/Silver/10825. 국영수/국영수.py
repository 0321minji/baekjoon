import sys
input=sys.stdin.readline

n=int(input())
students=[]
for i in range(n):
    students.append(input().split())

answer=sorted(students,key=lambda x:( -int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in answer:
    print(i[0])
