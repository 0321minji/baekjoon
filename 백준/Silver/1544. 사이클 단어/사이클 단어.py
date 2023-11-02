import sys
input=sys.stdin.readline

n=int(input())
word=[]
for i in range(n):
    word.append(input().rstrip())
result=[word[0]]
word.remove(word[0])

i=0
while True:
    if i>=len(word):
        break
    same=False
    for k in result:
        l=len(k)
        if len(word[i])==l and set(word[i])==set(k):
            for j in range(l):
                if k[j:]+k[:j]==word[i]:
                    same=True
                    break
    if not same:
        result.append(word[i])
        word.remove(word[i])
        i-=1
    i+=1

print(len(result))
