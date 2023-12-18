import sys
input=sys.stdin.readline

def solve():
    cnt=0
    mid=''

    for a,c in list(check.items()):
        if c%2==1:
            cnt+=1
            mid=a
            if cnt>1:
                print("I'm Sorry Hansoo")
                return
    result=''
    for a,c in sorted(check.items()):
        result+=(a*(c//2))
    result=result+mid+result[::-1]
    print(result)
    return
               
name=list(input().rstrip())
check={}

for i in name:
    if i not in check:
        check[i]=1
    else:
        check[i]+=1
solve()
