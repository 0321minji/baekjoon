import sys
input=sys.stdin.readline

n,k=map(int,input().split())
if k<5:
    print(0)
    exit()
elif k==26:
    print(n)
    exit()
    
word=[]
for i in range(n):
    word.append(list(set(input().rstrip())))
a=['a','n','c','t','i']
al=[0]*26
for i in a:
    al[ord(i)-ord('a')]=1
    ##a에 있는 알파벳은 1으로 초기화
result=0

def solve(index,count):
    global result

    if count==k-5:
        read=0
        for w in word:
            check=True
            for ww in w:
                if not al[ord(ww)-ord('a')]:
                    check=False
                    break
            if check:
                read+=1
        result=max(result,read)
        return
    
    for i in range(index,26):
        if not al[i]:
            al[i]=True
            solve(i,count+1)
            al[i]=False
solve(0,0)
print(result)
        