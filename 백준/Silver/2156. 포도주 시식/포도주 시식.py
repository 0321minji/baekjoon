n=int(input())
g=[]
for i in range(n):
    g.append(int(input()))

dp=[0]*(n)
dp[0]=g[0]


for i in range(1,n):
    if i<2:
        dp[1]=g[0]+g[1]
    elif i<3:
        dp[2]=max(dp[1],dp[0]+g[2],g[1]+g[2])
    else:
        dp[i]=max(dp[i-3]+g[i-1]+g[i],dp[i-2]+g[i],dp[i-1])
    
print(dp[n-1])
