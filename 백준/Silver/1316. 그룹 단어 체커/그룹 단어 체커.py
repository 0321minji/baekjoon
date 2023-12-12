import sys
input=sys.stdin.readline

def solve(string):
    global result
    alp=[]
    for i in string:
        if not i in alp:
            alp.append(i)
        else:
            if alp[-1]!=i:
                return
    result+=1
        


n=int(input())
result=0
for _ in range(n):
    string=list(input().rstrip())
    solve(string)

print(result)
