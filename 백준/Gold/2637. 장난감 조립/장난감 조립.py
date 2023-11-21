import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
m=int(input())
part=[[] for _ in range(n+1)]
result=[0]*(n+1)
result[n]=1
need=[0]*(n+1)

for _ in range(m):
    x,y,k=map(int,input().split())
    part[x].append([y,k])
    need[y]+=1

dq=deque([n])

#기본 부품 번호
origin=[i for i in range(1,n+1) if not part[i]]

while dq:
    temp=dq.popleft()
    for nxt, cnt in part[temp]:
        need[nxt]-=1
        result[nxt]+=cnt*result[temp]

        if not need[nxt]:
            dq.append(nxt)
for i in origin:
    print(i,result[i])
