import sys
input=sys.stdin.readline
sys.recursionlimit=10**8

def find(x,parent):
    
    if x!=parent[x]:
        parent[x]=find(parent[x],parent)
    return parent[x]

def union(x,y,parent):
    a=find(x,parent)
    b=find(y,parent)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
def dist(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5

n,m=map(int,input().split())

graph=[list(map(int,input().split())) for _ in range(n)]
graph.insert(0,[0,0])
parent=[i for i in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    union(a,b,parent)

check=[]
for i in range(1,len(graph)-1):
    for j in range(i+1,len(graph)):
        check.append([dist(graph[i],graph[j]),i,j])
check.sort()

result=0

for temp in check:
    cost,a,b=temp[0],temp[1],temp[2]
    #print(a,b,parent)
    if find(a,parent)!=find(b,parent):
        union(a,b,parent)
        result+=cost
print("{:.2f}".format(result))
