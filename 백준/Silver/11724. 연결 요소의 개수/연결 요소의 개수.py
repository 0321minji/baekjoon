import sys
input = sys.stdin.readline

def find(now):
    global res
    visit[now]=1
    for nxt in graph[now]:
        if not visit[nxt]:
            find(nxt)

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt=0
visit=[0]*(n+1)
for i in range(1,n+1):
    if not visit[i]:
        cnt+=1
        find(i)
print(cnt)