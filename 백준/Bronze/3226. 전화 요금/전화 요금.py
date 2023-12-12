import sys
input=sys.stdin.readline

def solve(h,m,d):
    global result
    if h==6 or h==18:
        if 60-m>d:
            if h==6:
                result+=d*5
            else:
                result+=d*10
        else:
            if h==6:
                result+=(60-m)*5
                result+=((m+d)%60)*10
            else:
                result+=(60-m)*10
                result+=((m+d)%60)*5
    elif 7<=h<=17:
        result+=d*10
    else:
        result+=d*5
    return
result=0
n=int(input())
for _ in range(n):
    call=list(map(str,input().split()))
    solve(int(str(call[0][:2])),int(str(call[0][3:])),int(call[1]))
    
print(result)
