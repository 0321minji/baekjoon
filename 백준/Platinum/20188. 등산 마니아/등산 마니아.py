import sys
from collections import defaultdict
input=sys.stdin.readline

n=int(input())
tree=defaultdict(list)
dp=defaultdict(list)
for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
visited=[False]*(n+1)
def dfs(index,route,dist):
    # print(index,dist)
    if not dp[index] or dp[index][0]>dist:
        dp[index]=[dist,route]
        
    # leaf이면 종료
    if len(tree[index])==1 and index!=1:
        return
    
    for nxt in tree[index]:
        if not visited[nxt]:
            visited[nxt]=True
            dfs(nxt,route|set([nxt]),dist+1)
            visited[nxt]=False

dfs(1,set(),0)
# print(dp)
res=0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        # print(i,j,dp[i][1]|dp[j][1])
        res+=len(dp[i][1]|dp[j][1])
print(res)