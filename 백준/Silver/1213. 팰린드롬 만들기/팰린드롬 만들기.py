import sys
import collections
input=sys.stdin.readline


name=input().rstrip()

cnt=0
result=''
mid='' #중간에 대칭되는 문자

check=collections.Counter(name) #Counter를 사용하여 딕셔너리로 바로 변환

for a,c in list(check.items()):
    if c%2==1:
        cnt+=1
        mid=a
        if cnt>1:
            print("I'm Sorry Hansoo")
            exit()

for a,c in sorted(check.items()):
    result+=a*(c//2)
result=result+mid+result[::-1]
print(result)
