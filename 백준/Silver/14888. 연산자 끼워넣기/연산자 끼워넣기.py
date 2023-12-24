import sys
input=sys.stdin.readline

def solve(i,temp,add,minus,mul,div):
    global MAX, MIN

    if i==n:
        if temp>MAX:
            MAX=temp
        if temp<MIN:
            MIN=temp
        return

    if add:
        solve(i+1,temp+a[i],add-1,minus,mul,div)
    if minus:
        solve(i+1,temp-a[i],add,minus-1,mul,div)
    if mul:
        solve(i+1,temp*a[i],add,minus,mul-1,div)
    if div:
        solve(i+1,int(temp/a[i]),add,minus,mul,div-1)
        


n=int(input())
a=list(map(int,input().split()))
cal=list(map(int,input().split()))

MAX=-10**9
MIN=10**9

solve(1,a[0],cal[0],cal[1],cal[2],cal[3])
print(MAX)
print(MIN)
