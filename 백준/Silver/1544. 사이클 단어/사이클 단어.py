import sys
input=sys.stdin.readline

def solve():
    word=[]
    for w in words:
        if not word:
            word.append(w)
        else:
            flag=False
            for i in range(len(w)):
                temp=w[i:]+w[:i]
                if temp in word:
                    flag=True
                    break
            if not flag:                
                word.append(w)

    return len(word)


n=int(input())
words=[input().rstrip() for _ in range(n)]
print(solve())
