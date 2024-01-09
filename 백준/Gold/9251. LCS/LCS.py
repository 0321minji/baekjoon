import sys
input=sys.stdin.readline

w1=input().rstrip()
w2=input().rstrip()

n=len(w1)
m=len(w2)
dp=[[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if w1[i-1]==w2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])
