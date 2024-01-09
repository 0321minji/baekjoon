import sys
input=sys.stdin.readline


n=int(input())
m=[int(input().rstrip()) for _ in range(n)]

dp=[0]*n
dp[0]=m[0]

for i in range(1,n):
    if i<2:
        dp[i]=m[0]+m[1]
    elif i<3:
        dp[i]=max(dp[1],dp[0]+m[2],m[1]+m[2])
    else:
        dp[i]=max(dp[i-3]+m[i-1]+m[i],dp[i-2]+m[i],dp[i-1])

print(dp[n-1])
