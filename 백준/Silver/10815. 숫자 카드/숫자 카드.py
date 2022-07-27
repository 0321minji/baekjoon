import sys
input=sys.stdin.readline

n=int(input())
get=list(map(int,input().split()))
m=int(input())
num=list(map(int,input().split()))
get.sort()
def solve(index,left,right):
    while left<=right:
        mid=(left+right)//2
        if get[mid]==num[index]:
            return mid
        elif get[mid]>num[index]:
            right=mid-1
        else:
            left=mid+1

    return None

for i in range(m):
    if solve(i,0,n-1) is None:
        print(0,end=' ')
    else:
        print(1,end=' ')
