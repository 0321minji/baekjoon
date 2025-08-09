import sys
input=sys.stdin.readline

m,n,l=map(int,input().split())

hunts=list(map(int,input().split()))
hunts.sort()
ani=[list(map(int,input().split())) for _ in range(n)]
# ani.sort()
cnt=0

def binary(x,l):
    left=0
    right=m-1
    
    while left<=right:
        mid=(left+right)//2
        if abs(x-hunts[mid])<=l:
            return True
        else:
            if x>hunts[mid]:
                left=mid+1
            else:
                right=mid-1
    return False
        

for x,y in ani:
    if binary(x,l-y):
        cnt+=1
print(cnt)