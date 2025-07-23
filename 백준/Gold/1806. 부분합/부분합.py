n,s=map(int,input().split())
nums=list(map(int,input().split()))

#투포인터
left=right=0
x=nums[left]
ans=n+1
while True:
    if right==n:
        break
    if x<s:
        right+=1
        if right>=n:
            break
        x+=nums[right]
    else:
        if left==right:
            ans=1
            break
        ans=min(ans,right-left+1)
        x-=nums[left]
        left+=1

print(ans if ans!=n+1 else 0)
        