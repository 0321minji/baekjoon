import sys
input=sys.stdin.readline

n,m,a,b=map(int,input().split())
interval=[list(map(int,input().split())) for _ in range(m)]
dp=[float('inf')]*(n+1)
dp[a]=1
dp[b]=1
check=[True]*(n+1)
for s,e in interval:
    check[s:e+1]=[False]*(e-s+1)
    if s<=a<=e:
        dp[a]=float('inf')
    if s<=b<=e:
        dp[b]=float('inf')
# print(check)
start=min(a,b)
for i in range(start,n+1):
    if not check[i]:
        continue
    dp[i]=min(dp[i-a]+1,dp[i-b]+1,dp[i])

print(dp[-1] if dp[-1]<float('inf') else -1)