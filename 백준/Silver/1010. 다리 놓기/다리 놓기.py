t=int(input())

for i in range(t):
    n,m=map(int,input().split())
    dp=[[0]*(m+1) for _ in range(n+1)]
    for j in range(1,n+1):
        for k in range(1,m+1):
            if j==1:
                dp[j][k]=k
                continue
            if j==k:
                dp[j][k]=1
            else:
                if k>j:
                    dp[j][k]=dp[j][k-1]+dp[j-1][k-1]

    print(dp[n][m])
 
   
