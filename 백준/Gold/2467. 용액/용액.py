import sys

input=sys.stdin.readline

n=int(input())
g=list(map(int,input().split()))

left=0
right=n-1
res=abs(g[left]+g[right])
ans=[g[left],g[right]]

while left<right:
    temp=g[left]+g[right]
    if temp==0:
        ans=[g[left],g[right]]
        break
    if abs(temp)<res:
        res=abs(temp)
        ans=[g[left],g[right]]
    
    if temp>0:
        right-=1
    else:
        left+=1

ans.sort()
print(*ans)