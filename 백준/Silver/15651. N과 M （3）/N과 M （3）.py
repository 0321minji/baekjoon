import sys
input=sys.stdin.readline

n,m=map(int,input().split())

res=[]

def bt(depth,now):
    if depth==m:
        res.append(now)
        return
    
    for i in range(1,n+1):
        bt(depth+1,now+[i])
    
bt(0,[])
for r in res:
    print(*r)