import sys
from collections import deque
input=sys.stdin.readline

def solve(p,node):
    q=deque([])
    q.append(p)
    visit=[-1]*(n+1)
    visit[p]=0

    while q:
        x=q.popleft()
        for nxt, w in tree[x]:
            if visit[nxt]==-1:
                visit[nxt]=visit[x]+w
                q.append(nxt)
    #print(visit)
    if node==1:
        return visit.index(max(visit))
    else:
        return max(visit)
        
n=int(input())
tree=[[] for _ in range(n+1)]
result=0
visit=[0]*(n+1)
for _ in range(n-1):
    a,b,c=map(int,input().split())
    tree[a].append([b,c])
    tree[b].append([a,c])

#1번 노드로부터 가장 큰 가중치를 가진 노드
index=solve(1,1)
#해당 노드로부터 다시 탐색 => 가장 긴 지름
print(solve(index,2))
