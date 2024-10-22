import sys
input=sys.stdin.readline

string=list(input().rstrip())
#print(string)

mid=len(string)//2

def solve(n):
    if len(string)%2:
        left=string[:mid+1-n]
    else:
        left=string[:mid-n]
    right=string[mid:len(string)-n]
    #print(left,right)

    return left!=right[::-1]
    

if solve(0):
    print(len(string))
elif solve(1):
    print(len(string)-1)
else:
    print(-1)
