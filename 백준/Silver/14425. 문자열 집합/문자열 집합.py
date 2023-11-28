import sys
input=sys.stdin.readline

n,m=map(int,input().split())
s=set([input().rstrip() for _ in range(n)])
result=0   
for i in range(m):
    temp=input().rstrip()
    if temp in s:
        result+=1
print(result)
