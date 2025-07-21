from collections import deque

n,k=map(int,input().split())

#0-1bfs
def bfs(n,k):
    MAX=100001
    dist=[float("inf")]*MAX
    dist[n]=0
    que=deque([n])
    
    while que:
        now=que.popleft()
        
        if now==k:
            return dist[k]
        # 순간이동 0
        if 0<=now*2<MAX and dist[now*2]>dist[now]:
            dist[now*2]=dist[now]
            que.appendleft(now*2)
        
        # 걷기 1
        for i in (now+1,now-1):
            if 0<=i<MAX and dist[i]>dist[now]+1:
                dist[i]=dist[now]+1
                que.append(i)

print(bfs(n,k))