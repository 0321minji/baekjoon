import sys
input=sys.stdin.readline

def solve():
    h=10**18
    l=1

    result=h

    while h>=l:
        mid=(h+l)//2
        s=0
        for i in range(n):
            s+=mid//t[i]
            if s>=m: break
        if s>=m:
            if mid<result:
                result=mid
            h=mid-1
        else:
            l=mid+1
    return result

n,m=map(int,input().split())
t=[int(input().rstrip()) for _ in range(n)]

print(solve())
