import sys
input=sys.stdin.readline

def check(i,j,x,y):
    result=0
    for a in range(i-1,x):
        for b in range(j-1,y):
            result+=arr[a][b]
    return result

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
#print(arr)

k=int(input())
for _ in range(k):
    i,j,x,y=map(int,input().split())
    print(check(i,j,x,y))
