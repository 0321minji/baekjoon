from itertools import combinations
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
numbers=list(map(int,input().split()))

result=0

for i in combinations(numbers,3):
    temp=sum(i)
    if temp>m:
        continue
    if temp==m:
        result=temp
        break
    result=max(result,temp)
print(result)
