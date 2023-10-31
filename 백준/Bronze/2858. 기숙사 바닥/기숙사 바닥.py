import sys
input=sys.stdin.readline

r,b=map(int,input().split())

t=r+b

for i in range(3,t//2):
    if t%i!=0:
        continue
    temp=t//i
    if (i-2)*(temp-2)==b:
        print(temp,i)
        break
    
