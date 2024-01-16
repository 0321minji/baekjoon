import sys
input=sys.stdin.readline
from collections import deque

def solve(p,t):
    que=deque([])
    que.append(p)
    visit=[-1]*(n+1)
    visit[p]=0

    while que:
        x=que.popleft()
        for nxt, wei in tree[x]:
            if visit[nxt]==-1:
                visit[nxt]=visit[x]+wei
                que.append(nxt)
    
    if t==1:
        return visit.index(max(visit))
    return max(visit)

n=int(input())
tree=[[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c=map(int,input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))

#1로부터 가장 먼 거리에 있는 (가장 큰 가중치의) 정점
index=solve(1,1)
#해당 정점으로 부터 가장 먼 거리에 있는~>.
print(solve(index,2))
