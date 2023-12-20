import sys
input=sys.stdin.readline

def solve(s):
    i=r
    while True:
        temp=s//i
        if temp>i:
            break
        
        if (i-2)*(temp-2)==b:
            print(i,temp)
            return
        i-=1
    

r,b=map(int,input().split())
solve(r+b)
