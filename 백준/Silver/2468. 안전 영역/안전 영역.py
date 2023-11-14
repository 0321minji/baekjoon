import sys
input=sys.stdin.readline

move=[[0,1],[0,-1],[1,0],[-1,0]]

def solve(a,b,k,visit):
    st=[[a,b]]
    while st:
        x,y=st.pop()
        for a,b in move:
            nx=x+a; ny=y+b;
            if 0<=nx<n and 0<=ny<n and h[nx][ny]>k and not visit[nx][ny]:
                st.append([nx,ny])
                visit[nx][ny]=1
                

    
n=int(input())
h=[list(map(int,input().split())) for _ in range(n)]

result=0
height=max(map(max,h))

for k in range(height):
    temp=0
    visit=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if h[i][j]>k and not visit[i][j]:
                solve(i,j,k,visit)
                temp+=1
                visit[i][j]=1

    result=max(temp,result)

print(result)
