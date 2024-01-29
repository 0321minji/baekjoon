import sys
input=sys.stdin.readline

def solve(a,b):
    r=b%a
    if not r:
        return a
    return solve(r,a)
    

n,m=map(int,input().split(':'))
result=solve(max(n,m),min(n,m))
print(str(n//result)+':'+str(m//result))
