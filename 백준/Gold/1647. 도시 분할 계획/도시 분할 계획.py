#kruskal

import sys
input=sys.stdin.readline


def find(x):
    if x!=p[x]:
        p[x]=find(p[x])
    return p[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return
    if rank[a]>rank[b]:
        p[b]=a
    elif rank[a]<rank[b]:
        p[a]=b
    else:
        p[a]=b
        rank[b]+=1


n,m=map(int,input().split())
graph=[]
p=[i for i in range(n+1)]
rank=[0]*(n+1)

for _ in range(m):
    a,b,c=list(map(int,input().split()))
    graph.append((a,b,c))

graph.sort(key=lambda x: x[2])
#비용 정렬

ans=0
end=0

for i in graph:
    if find(i[0])!=find(i[1]):
        union(i[0],i[1])
        ans+=i[2]
        end=i[2]
print(ans-end)
