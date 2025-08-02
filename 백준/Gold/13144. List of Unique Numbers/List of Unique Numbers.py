import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
nums=list(map(int,input().split()))
temp=[False for _ in range(n+1)]
cnt=0
left=0
right=0
while left<n and right<n:
    # print(temp,left,right,cnt)
    if not temp[nums[right]]:
        temp[nums[right]]=True
        right+=1
        cnt+=(right-left)
    else:
        temp[nums[left]]=False
        left+=1
print(cnt)