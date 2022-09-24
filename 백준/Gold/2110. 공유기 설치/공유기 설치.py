import sys
input=sys.stdin.readline

n,c=map(int,input().split())

x=[int(input()) for _ in range(n)]

x.sort()
left=1
right=x[-1]-x[0]

def count(dist,x):
    cnt=1
    pos=x[0]
    for i in x:
        if i-pos>=dist:
            cnt+=1
            pos=i
    return cnt
    
def solve(l,r,target,house):
    while(l<=r):
        mid=(l+r)//2
        installed=count(mid,house)

        if installed>=target:
            l=mid+1 #거리 늘려도 됨
        else:
            r=mid-1 #거리 줄이기

    return l
print(solve(left,right,c,x)-1)
