import sys
input=sys.stdin.readline

move=[[0,1],[0,-1],[1,0],[-1,0]]

def check(x,y,visit):
    for a,b in move:
        nx=x+a
        ny=y+b
        if [nx,ny] in visit:
            return False
    return True

def solve(visit,total):
    global result
    if total>=result: return
    if len(visit)==15:
        result=min(total,result)
    else:
        for i in range(1,n-1):
            for j in range(1,n-1):
                if check(i,j,visit) and (i,j) not in visit:
                    temp=[[i,j]]
                    temp_cost=money[i][j]
                    for a,b in move:
                        nx=i+a
                        ny=j+b
                        temp.append([nx,ny])
                        temp_cost+=money[nx][ny]
                    solve(visit+temp,total+temp_cost)
                
n=int(input())

money=[]
visit=[]
result=10**8
for _ in range(n):
    money.append(list(map(int,input().split())))
solve(visit,0)
print(result)
