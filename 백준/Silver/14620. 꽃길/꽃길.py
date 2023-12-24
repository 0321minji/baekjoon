import sys
input=sys.stdin.readline

def check(visit,x,y):
    for a,b in move:
        nx=x+a; ny=y+b
        if [nx,ny] in visit:
            return False
    return True

def solve(visit,total):
    global result

    if total>=result:
        return
    if len(visit)==15:
        result=min(result,total)
        return
    else:
        for i in range(1,n-1): ##가장 끝 줄은 어차피 못심음
            for j in range(1,n-1):
                if check(visit,i,j) and (i,j) not in visit:
                    temp=[[i,j]]
                    temp_cost=cost[i][j]
                    for a,b in move:
                        nx=i+a; ny=j+b
                        temp.append([nx,ny])
                        temp_cost+=cost[nx][ny]
                    solve(visit+temp,total+temp_cost)
    
n=int(input())
move=[[0,1],[0,-1],[1,0],[-1,0]]
cost=[list(map(int,input().split())) for _ in range(n)]
visit=[]
result=10**8

solve(visit,0)
print(result)
