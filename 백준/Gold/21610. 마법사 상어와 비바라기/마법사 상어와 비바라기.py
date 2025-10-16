import sys
input=sys.stdin.readline

n,m=map(int,input().split())
a=[ list(map(int,input().split())) for _ in range(n)]
ds = [list(map(int,input().split())) for _ in range(m)]

d={1:(0,-1),2:(-1,-1),3:(-1,0),4:(-1,1),5:(0,1),6:(1,1),7:(1,0),8:(1,-1)}

def move(cloud,dirs):
    di,dj=d[dirs[0]]
    s=dirs[1]

    moved=set()
    for i,j in cloud:
        ni=(i+di*s)%n
        nj=(j+dj*s)%n
        moved.add((ni,nj))
    return moved

def rain(cloud):
    for i,j in cloud:
        a[i][j]+=1

def water(cloud):
    move=[(-1,-1),(1,1),(-1,1),(1,-1)]
    for i,j in cloud:
        cnt=0
        for di,dj in move:
            ni=i+di; nj=j+dj
            if 0<=ni<n and 0<=nj<n and a[ni][nj]>0:
                cnt+=1
        a[i][j]+=cnt
        

def create(cloud):
    new=set()
    for i in range(n):
        for j in range(n):
            if a[i][j]>=2 and (i,j) not in cloud:
                new.add((i,j))
                a[i][j]-=2
    
    return new

new = {(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)}

for i in range(m):
    cloud=move(new,ds[i])
    rain(cloud)
    water(cloud)
    new=create(cloud)

res=0
for aa in a:
    res+=sum(aa)
print(res)