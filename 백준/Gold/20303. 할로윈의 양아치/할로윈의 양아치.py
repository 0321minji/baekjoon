import sys
from collections import deque, defaultdict
input=sys.stdin.readline

n,m,k=map(int,input().split())
candy=list(map(int,input().split()))
candy.insert(0,0)
f=defaultdict(list)

dp=[[0]*(k+1) for _ in range(2)]
visit=[True]*(n+1)
table=[]

for i in range(m):
    a,b=map(int,input().split())
    f[a].append(b)
    f[b].append(a)

for i in range(1,n+1):
    if visit[i]:
        visit[i]=False
        que=deque([i])
        count,result=0,0
        while(que):
            node=que.popleft()
            count+=1
            result+=candy[node]
            for to in f[node]:
                if visit[to]:
                    visit[to]=False
                    que.append(to)
        table.append((count,result))
for count,result in table:
    for i in range(0,k+1):
        if i>=count:
            dp[1][i]=max(dp[0][i],dp[0][i-count]+result)
        else:
            dp[1][i]=dp[0][i]
    for i in range(0,k+1):
        dp[0][i]=dp[1][i]

print(dp[1][k-1])