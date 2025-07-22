import sys
from collections import deque

input=sys.stdin.readline

t=int(input())
stickers=[[],[]]

for _ in range(t):
    n=int(input())
    answer=0
    stickers[0]=list(map(int,input().split()))
    stickers[1]=list(map(int,input().split()))
    dp=[[0 for _ in range(n)] for _ in range(2)]
    
    dp[0][0]=stickers[0][0]
    dp[1][0]=stickers[1][0]
    for j in range(1,n):
        dp[0][j]=max(dp[1][j-1]+stickers[0][j],dp[0][j-1])
        dp[1][j]=max(dp[0][j-1]+stickers[1][j],dp[1][j-1])
    print(max(map(max,dp)))
    