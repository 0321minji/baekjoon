import sys
input=sys.stdin.readline

def solve(h,m,d):
    if 7<=h<=17:
        return d*10
    if 0<=h<=5 or 19<=h<=23:
        return d*5
    if h==6 or h==18:
        if m+d>60:
            temp=(m+d)%60
            if h==6:
                return (d-temp)*5 + temp*10
            else:
                return temp*5 + (d-temp)*10
        elif h==6:
            return d*5
        return d*10
        
n=int(input())
result=0
for _ in range(n):
    time,d=list(map(str,input().split()))
    h=int(time[:2])
    m=int(time[3:])
    d=int(d)
    tmp=solve(h,m,d)
    
    result+=tmp
print(result)
