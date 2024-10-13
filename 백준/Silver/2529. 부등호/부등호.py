import sys
input=sys.stdin.readline

## dfs로..
## 최소 최대를 둘 다 구해야함 -> 가능한 모든 경우 구해서 정렬

def check(x,y,eq):
    if eq=='>' and x<y:
        return False
    if eq=='<' and x>y:
        return False
    return True

def solve(depth,now):
    if depth==k+1:
        temp.append(now)
        return 
    for i in range(10):
        ## 방문체크
        if visit[i]:
            continue
        ## 첫 숫자이거나, 조건에 맞는 경우 추가
        if depth==0 or check(now[depth-1],str(i),arr[depth-1]):
            visit[i]=1
            solve(depth+1,now+str(i))
            visit[i]=0

k=int(input())
arr=list(map(str,input().split()))
visit=[0]*(10)
temp=[]
solve(0,'')
temp.sort()

print(temp[-1])
print(temp[0])
