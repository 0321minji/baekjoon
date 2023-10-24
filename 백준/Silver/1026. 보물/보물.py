import sys
input=sys.stdin.readline


n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
##b 정렬 불가 ..?? ㅁㄹㄹ몸ㄹ라재배열할거임
b=sorted(b,reverse=True)
a.sort()

s=0
for i in range(n):
    s+=a[i]*b[i]

print(s)

