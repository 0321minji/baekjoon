import sys, math
input=sys.stdin.readline

def dfs(st,now,v,level):
    global result
    # level==n 이면 자기 자신으로 돌아가야함
    if level==n:
        # [now][st]가 0 이면 잘못된 경
        if w[now][st]:
            v+=w[now][st]
            if result>v:
                result=v
        return
    
    #갱신 필요 X
    if v > result:
        return

    for i in range(n):
        if not visit[i] and w[now][i]:
            visit[i]=1
            dfs(st,i,v+w[now][i],level+1)
            visit[i]=0
    
    

n=int(input())
w=[list(map(int,input().split())) for _ in range(n)]
result=10**8
visit=[0]*n
for i in range(n):
    visit[i]=1
    dfs(i,i,0,1)
    visit[i]=0
print(result)
