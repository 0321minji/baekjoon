import sys

input=sys.stdin.readline

n=int(input())
nums=list(map(int,input().split()))
dp=[[-1 for _ in range(n)] for _ in range(n)]
m=int(input())

for i in range(n):
    for j in range(i+1):
        dp[i][j]=1
        
def findDP(s,e):
    if dp[s][e]!=-1: return dp[s][e]
    if nums[s]!=nums[e]:
        dp[s][e]=0
        return 0
    
    if dp[s+1][e-1]==-1:
        dp[s+1][e-1] = findDP(s+1,e-1)
    dp[s][e]=dp[s+1][e-1]
    return dp[s][e]


for _ in range(m):
    s,e=map(int,input().split())
    print(findDP(s-1,e-1))