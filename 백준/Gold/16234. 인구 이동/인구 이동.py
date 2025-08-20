import sys
input=sys.stdin.readline
from collections import deque
n,L,R=map(int,input().split())
people=[list(map(int,input().split())) for _ in range(n)]

move=[(0,1),(0,-1),(1,0),(-1,0)]


def calculate(country,count):
    res=count//len(country)
    for i,j in country:
        people[i][j]=res
    return
    
def check(i,j):
    # 연합 나라의 위치
    temp=[(i,j)] 
    # 연합의 인구수
    count=people[i][j]
    que=deque([(i,j)])
    while que:
        x,y=que.popleft()
        for dx,dy in move:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if L<=abs(people[x][y]-people[nx][ny])<=R:
                    visited[nx][ny]=True
                    count+=people[nx][ny]
                    temp.append((nx,ny))
                    que.append((nx,ny))
    if count!=people[i][j]:
        return temp,count
    return [],0
    
level=0
while True:
    state=[]
    visited=[[False] *(n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if  not visited[i][j]:
                visited[i][j]=True
                temp,count=check(i,j)
                if temp:
                    state.append((temp,count))
    if not state:
        break
    
    for country,count in state:
        calculate(country,count)
    level+=1
    # people=now

print(level)