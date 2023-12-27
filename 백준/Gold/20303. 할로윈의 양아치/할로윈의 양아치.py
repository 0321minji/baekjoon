import sys
from collections import deque
input=sys.stdin.readline

def solve():
    global temp
    visit=[0]*(n+1)
    for i in range(1,n+1):
        if not visit[i]:
            visit[i]=1
            que=deque([i])
            count,result=0,0
            while que:
                node=que.popleft()
                count+=1
                result+=c[node]
                for to in graph[node]:
                    if not visit[to]:
                        visit[to]=1
                        que.append(to)
            temp.append((count,result))
    return dynamic()
    
    
def dynamic():
    dp=[[0]*(k+1) for _ in range(2)]
    for count,result in temp:
        for i in range(0,k+1):
            if i>=count:
                dp[1][i]=max(dp[0][i],dp[0][i-count]+result)
            else:
                dp[1][i]=dp[0][i]
        for i in range(0,k+1):
            dp[0][i]=dp[1][i]
    #print(dp)
    return dp[1][k-1]

n,m,k=map(int,input().split())
c=list(map(int,input().split()))
c.insert(0,0)
graph=[[] for _ in range(n+1)]
temp=[]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
print(solve())
