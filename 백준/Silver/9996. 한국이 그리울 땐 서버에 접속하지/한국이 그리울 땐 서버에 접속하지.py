import sys
input=sys.stdin.readline

n=int(input())
pattern = list(map(str,input().rstrip().split("*")))

def checkPattern(word):
    l1=len(pattern[0])
    l2=len(pattern[1])
    if len(word)<l1+l2:
        return "NE"
    else:
        if(word[:l1]==pattern[0] and word[-l2:]==pattern[1]):
            return "DA"
    return "NE"
for _ in range(n):
    word=input().rstrip()
    print(checkPattern(word))