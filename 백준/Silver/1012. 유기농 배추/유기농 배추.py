import sys
input=sys.stdin.readline

move=[[0,1],[0,-1],[1,0],[-1,0]]

def check(a,b):
    st=[[a,b]]
    while st:
        x,y=st.pop()
        for a,b in move:
            nx=x+a; ny=y+b
            if 0<=nx<m and 0<=ny<n and ground[nx][ny]:
                st.append([nx,ny])
                ground[nx][ny]=0


t=int(input())
for _ in range(t):
    snail=0
    m,n,k=map(int,input().split())
    ground=[[0]*(n) for _ in range(m)]
    for _ in range(k):
        x,y=map(int,input().split())
        ground[x][y]=1

    for i in range(m):
        for j in range(n):
            if ground[i][j]:
                check(i,j)
                snail+=1
    print(snail)
