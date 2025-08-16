import sys
input=sys.stdin.readline
n,k=map(int,input().split())

dp=[float('INF')]*(n+1)
dp[0]=0
for i in range(1,n+1):
    dp[i]=min(dp[i],dp[i-1]+1)
    if i+i//2<=n:
        dp[i+i//2]=min(dp[i+i//2],dp[i]+1)

print("minigimbob" if dp[-1] <=k else 'water')