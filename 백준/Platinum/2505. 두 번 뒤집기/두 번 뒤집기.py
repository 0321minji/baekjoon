import sys

input=sys.stdin.readline
n=int(input())
nums=[0]+list(map(int,input().split()))
temp=nums[:]
left=[]
right=[]
for i in range(1,n+1):
    if len(left)>2:
        left=[]
        break
    if nums[i]!=i:
        end=nums.index(i)
        nums[i:end+1]=nums[i:end+1][::-1]
        left.append((i,end))


nums=temp[:]
for i in range(n,0,-1):
    if len(right)>2:
        right=[]
        break
    if nums[i]!=i:
        start=nums.index(i)
        nums[start:i+1]=nums[start:i+1][::-1]
        right.append((start,i))
    
ans=list(set(left+right))

while len(ans)<2:
    ans.append((1,1))

for a in ans:
    print(*a)