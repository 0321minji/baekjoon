import sys
input=sys.stdin.readline
n,k=map(int,input().split())

people=[0]*n
result=0
pair=[0]*21
for i in range(n):
    #이름 길이 저장
    name=len(input())-1
    # i번째 이름의 길이
    people[i]=name

    #등수 차이 k 초과이면 i-k-1번째 pair 값 -1
    if i>k:
        pair[people[i-k-1]]-=1
    #해당 길이에 대한 쌍 더하기
    result+=pair[name]
    #자기 자신
    pair[name]+=1

print(result)
    
