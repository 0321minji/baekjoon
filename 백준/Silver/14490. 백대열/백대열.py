import sys
input=sys.stdin.readline

def gcd(a,b):
    r=b%a
    if not r:
        return a
    
    return gcd(r,a)

n,m=map(int,input().split(':'))
temp=gcd(n,m)
print(f"{n//temp}:{m//temp}")
