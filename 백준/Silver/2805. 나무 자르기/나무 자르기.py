from bisect import bisect_left
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
trees=list(map(int,input().split()))
trees.sort()

left=1
right=trees[-1]
res=0
while left<=right:
    mid=(left+right)//2
    idx=bisect_left(trees,mid)
    
    total=sum(h-mid for h in trees[idx:])
    if total>=m:
        left=mid+1
        res=mid
    else:
        right=mid-1

print(res)