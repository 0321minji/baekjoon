import sys
input=sys.stdin.readline

'''
이전 동전을 이용해서 만들 수 있는 경우의 수 +
지금 동전을 이용해서 만들 수 있는 경우의 수 = 금액 m을 만들 수 있는 경우의 수
'''


t=int(input())
for i in range(t):
    n=int(input())
    coins=list(map(int,input().split()))
    m=int(input())

    #memoization
    dp=[0]*(m+1)
    dp[0]=1

    for c in coins:
        for i in range(m+1):
            if i>=c:
                dp[i]+=dp[i-c]

    print(dp[m])
