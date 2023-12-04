import sys
input=sys.stdin.readline

n,m=map(int,input().split(':')) #: 사이에 있는거 빼먹지 말기

def gcd(a,b): #유클리드 호제법 사용
    while b>0:
        temp=a
        a=b
        b=temp%b
    return a

a=gcd(n,m)

print(str(n//a)+":"+str(m//a))
