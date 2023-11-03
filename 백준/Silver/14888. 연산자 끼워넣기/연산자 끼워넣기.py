import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
cal=list(map(int,input().split()))

def solve(i,temp,add,minus,mul,div):
    global MAX, MIN
    if i==n:
        MAX=max(temp,MAX)
        MIN=min(temp,MIN)
        return
    
    if add:
        solve(i+1,temp+a[i],add-1,minus,mul,div)
    if minus:
        solve(i+1,temp-a[i],add,minus-1,mul,div)
    if mul:
        solve(i+1,temp*a[i],add,minus,mul-1,div)
    if div:
        solve(i+1,int(temp/a[i]),add,minus,mul,div-1)

MAX=-10**9
MIN=10**9
solve(1,a[0],cal[0],cal[1],cal[2],cal[3])
print(MAX)
print(MIN)
