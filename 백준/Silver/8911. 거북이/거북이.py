import sys
input=sys.stdin.readline

def solve(case):
    x=0
    y=0
    hx=lx=hy=ly=0
    direct=0

    for i in case:
        if i=='L':
            direct-=1
            direct%=4
        elif i=='R':
            direct+=1
            direct%=4
        else:
            if (direct==0 and i=='F') or (direct==2 and i=='B'):
                y+=1
                hy=max(hy,y)
            elif (direct==1 and i=='F') or (direct==3 and i=='B'):
                x+=1
                hx=max(hx,x)
            elif (direct==2 and i=='F') or (direct==0 and i=='B'):
                y-=1
                ly=min(ly,y)
            else:
                x-=1
                lx=min(lx,x)
    return (hx-lx)*(hy-ly)
t=int(input())
for _ in range(t):
    case=list(input().rstrip())
    print(solve(case))
