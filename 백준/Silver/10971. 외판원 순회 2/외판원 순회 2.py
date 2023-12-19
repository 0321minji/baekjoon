import sys
input=sys.stdin.readline

def solve(start,now,w,level):
    global result
    if level==n:
        if load[now][start]:
            w+=load[now][start]
            if result>w:
                result=w
        return

    if w>result:
        return

    for i in range(n):
        if not visit[i] and load[now][i]:
            visit[i]=1
            solve(start,i,w+load[now][i],level+1)
            visit[i]=0

n=int(input())
load=[list(map(int,input().split())) for _ in range(n)]
result=10**7
visit=[0]*n

for i in range(n):
    visit[i]=1
    solve(i,i,0,1)
    visit[i]=0
print(result)
