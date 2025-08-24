import sys, heapq
from collections import defaultdict, deque
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
lands=defaultdict(set)

que=deque([])
move=[(0,1),(0,-1),(-1,0),(1,0)]

def find_land(index,x,y):
    que=deque([(x,y)])
    graph[x][y]=index
    lands[index].add((x,y))
    while que:
        x,y=que.popleft()
        for dx,dy in move:
            nx=x+dx; ny=y+dy
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                lands[index].add((nx,ny))
                graph[nx][ny]=index
                que.append((nx,ny))
    return

index=2
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            find_land(index,i,j)
            index+=1
cnt=len(lands)
bridges=dict()
edges=[]


def find_num(i,j):
    for index in lands:
        if (i,j) in lands[index]:
            return index
            
def find_bridges():
    for i in range(n):
        last_id = 0
        last_j = -1
        for j in range(m):
            if graph[i][j] >= 2:
                cur_id = graph[i][j]
                if last_id == 0:
                    last_id = cur_id
                    last_j = j
                else:
                    gap = j - last_j - 1
                    if gap >= 2 and last_id != cur_id:
                        a, b = sorted((last_id, cur_id))
                        bridges[(a, b)] = min(bridges.get((a, b), 101), gap)
                    last_id = cur_id
                    last_j = j

    for j in range(m):
        last_id = 0
        last_i = -1
        for i in range(n):
            if graph[i][j] >= 2:
                cur_id = graph[i][j]
                if last_id == 0:
                    last_id = cur_id
                    last_i = i
                else:
                    gap = i - last_i - 1
                    if gap >= 2 and last_id != cur_id:
                        a, b = sorted((last_id, cur_id))
                        bridges[(a, b)] = min(bridges.get((a, b), 101), gap)
                    last_id = cur_id
                    last_i = i

find_bridges()
for (x,y),value in bridges.items():
    edges.append([x,y,value])
edges.sort(key=lambda x:x[2])

def find_parent(parent,a):
    if parent[a]!=a:
        parent[a]=find_parent(parent,parent[a])
    return parent[a]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
parent=[0]*(cnt+2)
for i in range(cnt+2):
    parent[i]=i
# print(parent)
result=0
used_edges=0
for a,b,value in edges:
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result+=value
        used_edges += 1
        
print(result if used_edges==cnt-1 else -1)