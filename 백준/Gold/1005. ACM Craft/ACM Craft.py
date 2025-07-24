from collections import deque, defaultdict
import sys

input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    d=list(map(int,input().split()))
    graph = defaultdict(list)
    indegrees = [0]*(n+1)
    t=[0]*(n+1)
    
    for _ in range(k):
        a,b=map(int,input().split())
        graph[a].append(b)
        indegrees[b]+=1
    w=int(input())
    
    que=deque([])
    for i in range(1,n+1):
        if indegrees[i]==0:
            que.append([i,0])

    while que:
        num,time=que.popleft()
        time+=d[num-1]
        #print(num,time)
        if num==w:
            print(time)
            break        
    
        for i in graph[num]:
            indegrees[i]-=1
            t[i]=max(t[i],time)
            if indegrees[i]==0:
                que.append([i,t[i]])
    