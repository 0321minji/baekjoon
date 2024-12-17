import sys
input=sys.stdin.readline

## 오름차순 수열 -> +-공백 : ascii 순서 공백>+>->숫자
def solve(s,depth):
    if depth==n:
        #print(eval(s))
        if (eval(s.replace(' ',''))==0):
            print(s)
        return
    temp = num[depth]
    ## 1. 공백 ->  
    solve(s+' '+temp,depth+1)
    ## 2. +
    solve(s+'+'+temp,depth+1)
    ## 3. -
    solve(s+'-'+temp,depth+1)

t=int(input())
for _ in range(t):
    n=int(input())
    num=list(str(i) for i in range(1,n+1))
    temp=num[0]
    solve(temp,1)
    print()
