import sys

input=sys.stdin.readline

n=int(input())
num1=[]
num2=[]
v1=[];v2=[]

for i in range(n):
    temp=input().rstrip()
    num1.append(temp)

for i in range(n):
    temp=input().rstrip()
    num2.append(temp)


car=0

for i in range(n):
    for j in range(i+1,n):
        if(num1.index(num2[i])>num1.index(num2[j])):
            car+=1
            break

print(car)