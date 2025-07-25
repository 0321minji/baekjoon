import sys
input=sys.stdin.readline

s,e=map(int,input().split())
r=e-s+1
# 에라토스테네스의 체
def find(s,e):
    arr=[0]*r

    for i in range(2,int(e**0.5)+1):
        pow=i*i
        start=((s+pow-1)//pow)*pow
        
        for j in range(start,e+1,pow):
            arr[j-s]=1
    return sum(arr)
                
ans=r-find(s,e)
print(ans)