import sys
input=sys.stdin.readline

n,m=map(int,input().split())

res=[]
visited=[False]*(n+1)
def bt(depth,now):
    if depth==m:
        res.append(now)
        return    
    for i in range(1,n+1):
        if not visited[i]:
            visited[i]=True
            bt(depth+1,now+[i])
            visited[i]=False
    
bt(0,[])
for r in res:
    print(*r)