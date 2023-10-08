import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
def dfs(link,start,parents):
    for i in link[start]:
        if(parents[i]==0):
            parents[i]=start
            dfs(link,i,parents)
n=int(input())
link=[[] for _ in range(n+1)]

for i in range(n-1):
    a,b=map(int,input().split())
    link[a].append(b)
    link[b].append(a)

parents=[0]*(n+1)
dfs(link,1,parents)

for i in range(2,n+1):
    print(parents[i])

