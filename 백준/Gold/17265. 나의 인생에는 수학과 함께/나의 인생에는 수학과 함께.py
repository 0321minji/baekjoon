import sys
input=sys.stdin.readline

n=int(input())
board=[list(map(str,input().split())) for _ in range(n)]

min_res=float('inf')
max_res=-float('inf')

move=[[1,0],[0,1]]

def calculate(op1,op2,op):
    if op=='+':
        return op1+op2
    elif op=='-':
        return op1-op2
    elif op=='*':
        return op1*op2

visited=[[False]*n for _ in range(n)]

def dfs(i,j,res,level,st):
    global min_res, max_res
    # print(st,res)
    if level%2 and st:
        num=st.pop()
        op=st.pop()
        res=calculate(res,int(num),op)
    
    if i==j==n-1:
        min_res=min(min_res,res)
        max_res=max(max_res,res)
        return
    
    for di,dj in move:
        ni=i+di; nj=j+dj
        if 0<=ni<n and 0<=nj<n and not visited[ni][nj]:
            visited[ni][nj]=True
            dfs(ni,nj,res,level+1,st+[board[ni][nj]])
            visited[ni][nj]=False

visited[0][0]=True
dfs(0,0,int(board[0][0]),1,[])
print(max_res,min_res)