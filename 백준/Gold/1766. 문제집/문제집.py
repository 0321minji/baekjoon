import sys, heapq
input=sys.stdin.readline

n,m=map(int,input().split())

res=[]
graph=[[]for _ in range(n+1)]
indegree=[0]*(n+1)
que=[]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

for i in range(1,n+1):
    if indegree[i]==0:
        heapq.heappush(que,i)

while que:
    temp=heapq.heappop(que)
    res.append(temp)
    for i in graph[temp]:
        indegree[i]-=1
        if indegree[i]==0:
            heapq.heappush(que,i)
print(*res)
