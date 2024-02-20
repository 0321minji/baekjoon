import sys
input=sys.stdin.readline

n=int(input())

#1 1
#2 11 00 2
#3 111 100 001 3 
#4 1111 1100 0011 0000 1001 5

dp=[0]*(n+1)
if n==1:
    print(1)
    exit()
dp[1]=1
dp[2]=2
for i in range(3,n+1):
    temp=dp[i-1]+dp[i-2]
    temp%=15746
    dp[i]=temp
print(dp[n])
