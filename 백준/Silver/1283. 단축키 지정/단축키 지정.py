import sys

input=sys.stdin.readline

n=int(input())
dic=dict()
words=[list(map(str,input().split())) for _ in range(n)]
k=[]

# words[i]를 이룬 단어들에 대해 첫 글자 비교
# 왼쪽부터 비교
def check(i):
    global dic
    
    for j in range(len(words[i])):
        w=words[i][j]
        t=w[0].lower()
        if t not in k:
            k.append(t)
            words[i][j]='['+w[0]+']'+w[1:]
            return
    for z in range(len(words[i])):
        w=words[i][z]
        for j in range(len(w)):
            t=w[j].lower()
            if t not in k:
                k.append(t)
                words[i][z]=w[:j]+'['+w[j]+']'+w[j+1:]
                dic[i]=[t,j]
                return
    
for i in range(n):
    check(i)

# print(words)

for i in range(n):
    for w in words[i]:
        print(w,end=' ')
    print()