import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
sands=[list(map(int,input().split())) for _ in range(n)]
move=[(0,-1),(1,0),(0,1),(-1,0)]
res=0
remain=0
scatter_map = [
	[[0,0,2,0,0],
	 [0,10,7,1,0],
	 [5,0,0,0,0],
	 [0,10,7,1,0],
	 [0,0,2,0,0]]
	 ,
	[[0,0,0,0,0],
	[0,1,0,1,0],
	[2,7,0,7,2],
	[0,10,0,10,0],
	[0,0,5,0,0]]
	,
	[[0,0,2,0,0],
	[0,1,7,10,0],
	[0,0,0,0,5],
	[0,1,7,10,0],
	[0,0,2,0,0]]
	,
	[[0,0,5,0,0],
	[0,10,0,10,0],
	[2,7,0,7,2],
	[0,1,0,1,0],
	[0,0,0,0,0]]
]
def is_range(x,y):
    return 0<=x<n and 0<=y<n

def last(x,y,remain):
    global res
    if is_range(x,y):
        sands[x][y]+=remain
    else:
        res+=remain

def calculate(x,y,index):
    global res
    remain=sands[x][y]
    dir=scatter_map[index]
    a=0
    for i in range(x-2,x+3):
        b=0
        for j in range(y-2,y+3):
            temp=dir[a][b]*sands[x][y]//100
            remain-=temp
            if is_range(i,j):
                sands[i][j]+=temp
            else:
                res+=temp
            b+=1
        a+=1
    if index==0:
        last(x,y-1,remain)
    elif index==1:
        last(x+1,y,remain)
    elif index==2:
        last(x,y+1,remain)
    elif index==3:
        last(x-1,y,remain)
    sands[x][y]=0

def tornado():
    x=y=n//2
    index=0
    flag=False
    level=1
    
    while x>=0 and y>=0:
        if x==0:
            # x 0 될때까지 이동
            for i in range(y-1,-1,-1):
                calculate(x,i,index)
            return
        
        for _ in range(level):
            x+=move[index][0]
            y+=move[index][1]
            calculate(x,y,index)

        ## 다음 index 비교
        if not flag:
            flag=True
        else:
            level+=1
            flag=False
        index=(index+1)%4
tornado()
print(res)