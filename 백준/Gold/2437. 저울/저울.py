import sys
input=sys.stdin.readline

n=int(input())
m=list(map(int,input().split()))

m.sort()
result=1
for i in m:
    if result<i:
        break
    result+=i
print(result)
