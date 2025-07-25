import sys
from collections import Counter
input=sys.stdin.readline

n=int(input())
board=[[] for _ in range(n)]
res=0
for i in range(n):
    board[i]=list(input().rstrip())
    if Counter(board[i]).most_common(1)[0][1] == n:
        res=n
        
def check():
    global res
    for i in range(n):
        temp=1
        for j in range(1,n):
            if board[i][j-1]==board[i][j]:
                temp+=1
            else:
                res=max(res,temp)
                temp=1
        res=max(res,temp)

    for j in range(n):
        temp=1
        for i in range(1,n):
            if board[i-1][j]==board[i][j]:
                temp+=1
            else:
                res=max(res,temp)
                temp=1
        res=max(res,temp)

nxt=[[0,1],[1,0]]
i=0
while i<n and res<n:
    for j in range(n):
        for di,dj in nxt:
            ni=i+di; nj=j+dj
            if ni<n and nj<n and board[i][j]!=board[ni][nj]:
                board[i][j],board[ni][nj]=board[ni][nj],board[i][j]
                check()
                board[i][j],board[ni][nj]=board[ni][nj],board[i][j]
    i+=1

print(res)