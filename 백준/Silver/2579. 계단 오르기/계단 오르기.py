import sys
input=sys.stdin.readline

n=int(input())
s=[int(input().rstrip()) for _ in range(n)]
#print(s)

dp=[0]*(n)
## 특정 계단에 도달하는 방법
# 전전전계단 + 전계단 +나 or 그 전전계단+나
if n<=2:
    print(sum(s))
    exit()
dp[0]=s[0]
dp[1]=dp[0]+s[1]


for i in range(2,n):
    dp[i]=max(dp[i-3]+s[i-1]+s[i],dp[i-2]+s[i])

print(dp[-1])
