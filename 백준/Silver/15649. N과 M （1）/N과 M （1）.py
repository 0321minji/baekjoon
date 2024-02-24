import sys
input=sys.stdin.readline

def backtracking(level):
    global m
    if level==m:
        print(*temp[:level])
    for i in range(1,n+1):
        if not check[i]:
            check[i]=1
            temp[level]=i
            backtracking(level+1)
            check[i]=0
        #print(temp)


n,m=map(int,input().split())
temp=[0]*10
check=[0]*10

backtracking(0)
