import sys
input=sys.stdin.readline

def solve(n):
    result=0
    # n이 홀수 => 5가 홀수 개
    # n이 짝수 => 5가 짝수 개
    temp=n//5
    if n%2:
        if temp%2:
            result+=temp
            n-=5*temp
        else:
            if temp==0: return -1
            result+=(temp-1)
            n-=5*(temp-1)
    else:
        if temp%2:
            result+=(temp-1)
            n-=5*(temp-1)
        
        else:
            result+=temp
            n-=5*temp
    result+=n//2
    if n%2:
        return -1
    
    return result

n=int(input())
print(solve(n))