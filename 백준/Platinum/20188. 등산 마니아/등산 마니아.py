import sys
from collections import defaultdict
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
n=int(input())
tree=defaultdict(list)
dp=defaultdict(list)
for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

res=0
def dfs(index,parent):
    global res
    size=1
    
    for v in tree[index]:
        if v==parent:
            continue
        # 자기 밑의 정점 수 세기
        cnt=dfs(v,index)
        # 양 쪽에서
        res+=cnt*(n-cnt)
        # 밑 에서
        res+=cnt*(cnt-1)//2
        size+=cnt
    return size
    
dfs(1,0)
print(res)
