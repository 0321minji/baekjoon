import sys
input=sys.stdin.readline

move=[[0,1],[0,-1],[-1,0],[1,0]]

n=int(input())
money=[list(map(int,input().split())) for _ in range(n)]
visit=[]

def check(visit,x,y):
    for a,b in move:
        nx=x+a;
        ny=y+b
        if [nx,ny] in visit:
            return False
    return True

result=10**8
def solve(visit,total):
    global result
    if total>=result:
        #result 값보다 total이 더 큰 경우 무시
        return
    if len(visit)==15:##5*3 (3개의 씨앗을 다 심은 경우
        result=min(total,result)

    else:
        for i in range(1,n-1):
            for j in range(1,n-1): #어차피 맨 가장자리에 씨앗 심을 수 X
                if check(visit,i,j) and (i,j) not in visit: #방문체크
                    #씨앗 심을 위치 = temp
                    temp=[[i,j]]
                    temp_cost=money[i][j]
                    for a,b in move:
                        nx=i+a; ny=j+b
                        temp.append([nx,ny])
                        temp_cost+=money[nx][ny]
                    #해당 위치를 기준으로 5칸 값 탐색 => solve 호출해서 비교
                    solve(visit+temp,total+temp_cost)
solve(visit,0)
print(result)
