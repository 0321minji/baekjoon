import sys
input=sys.stdin.readline

n=int(input())
p=list(map(int,input().split()))
p.sort()
result=0
k=0
for i in p:
   k+=i
   result+=k

print(result)
