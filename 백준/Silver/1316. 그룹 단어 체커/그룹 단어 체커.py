import sys
input=sys.stdin.readline

def solve(word):
    global result
    alp=[]
    for i in word:
        if i in alp and alp[-1]!=i:
            return
        alp.append(i)
    result+=1
    
n=int(input())
result=0
for _ in range(n):
    solve(input().rstrip())
print(result)
