import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def solve(index,parent):
    for i in tree[index]:
        if not parent[i]:
            parent[i]=index
            solve(i,parent)
    
    
    
n=int(input())
tree=[[] for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

parent=[0]*(n+1)
parent[1]=1
solve(1,parent)
print(*parent[2:],sep='\n')

