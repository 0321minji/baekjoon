import sys
input=sys.stdin.readline

def solve(h,m,d):
    global result
    if 7<=h<=17:
        result+=d*10
    elif 0<=h<=5 or 19<=h<24:
        
        result+=d*5
    else:
        if (m+d)//60:
            t=(m+d)%60
            if h==18:
                result+=t*5
                result+=(d-t)*10
            else:
                result+=t*10
                result+=(d-t)*5
        else:
            if h==18:
                result+=d*10
            elif h==6:
                result+=d*5
            
        

n=int(input())
result=0
for _ in range(n):
    temp=list(map(str,input().split()))
    solve(int(str(temp[0][:2])),int(str(temp[0][3:])),int(temp[1]))
print(result)
