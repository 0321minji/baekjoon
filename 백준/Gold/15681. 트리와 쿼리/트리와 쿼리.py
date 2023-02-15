import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(now):
    global visit
    visit[now]=1
    for i in m[now]:
        if visit[i]==-1:
            visit[now]+=dfs(i)
    return visit[now]


n,r,q=map(int,input().split())
m=[[]for _ in range(n+1)]
visit=[-1]*(n+1)

for i in range(n-1):
    a,b=map(int,input().split())
    m[a].append(b)
    m[b].append(a)

dfs(r)
for _ in range(q):
    index=int(input())
    print(visit[index])
