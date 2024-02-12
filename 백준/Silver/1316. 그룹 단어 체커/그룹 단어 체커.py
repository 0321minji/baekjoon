import sys
input=sys.stdin.readline

def solve(word):
    global result
    s=set(word[0])
    for i in range(1,len(word)):
        if word[i] in s and word[i-1]!=word[i]:
            return
        s.add(word[i])
    result+=1
    
n=int(input())
words=[input().rstrip() for _ in range(n)]
result=0
for w in words:
    solve(w)
print(result)
