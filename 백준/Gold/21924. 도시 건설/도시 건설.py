import sys
input=sys.stdin.readline

def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]

def union(x,y):
    a=find(x)
    b=find(y)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

def solve(result):
    cnt=0

    for w,a,b in pq:
        if find(a)!=find(b):
            union(a,b)
            result-=w

    for i in range(1,n):
        if i==parent[i]:
            cnt+=1
            
    if cnt>1:
        return -1
    else:
        return result

n,m=map(int,input().split())
parent=[i for i in range(n+1)]
pq=[]
result=0

for _ in range(m):
    a,b,c=map(int,input().split())
    pq.append((c,a,b))
    result+=c
pq.sort()
print(solve(result))
