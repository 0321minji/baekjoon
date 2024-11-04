import sys
input=sys.stdin.readline

n=int(input())
par=list(map(int,input().split()))
delete=int(input())
tree=[[0]*(n) for _ in range(n)]
visit=[0]*n
count=0

def dfs(root):
    global count
    visit[root]=1
    temp=1
    for i in range(n):
        if(tree[root][i]==1 and visit[i]==0): #루트와 연결되어있고 방문한적 없음
            temp=0
            dfs(i)
    if temp==1:
        count+=1

for i in range(len(par)):
    if par[i]!=-1: #root가 아닐때
        tree[i][par[i]]=1
        tree[par[i]][i]=1 #부모와 자식노드 연결나타냄
    else: #root 일때
        root=i

for i in range(n):
    tree[i][delete]=0
    tree[delete][i]=0 #지울 노드와 연결된 값 0으로
dfs(root)

if delete==root:
    print(0)
else:
    print(count)
