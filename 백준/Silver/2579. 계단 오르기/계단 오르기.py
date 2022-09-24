import sys
input=sys.stdin.readline

n=int(input())
score=[0]*(301)

def solve(score):
    dp=[0]*(301)
    dp[1]=score[1]
    dp[2]=score[1]+score[2]

    for i in range(3,n+1):
        dp[i]=max(dp[i-3]+score[i-1],dp[i-2])+score[i]
    return dp[n]
for i in range(1,n+1):
    score[i]=int(input())

print(solve(score))
