import sys
input=sys.stdin.readline

n,k=map(int,input().split())
people=[]

for i in range(1,n+1):
    people.append(i)

result=[]
index=k-1

while people:
    #k번째 index 제거
    result.append(people.pop(index))
    #index 값 갱신 (리스트 길이 감소->%연산)
    if people:
        index=(index+k-1)%len(people)

print('<',end='')
for i in range(n):
    if i==n-1:
        print(result[i],end='>')
    else:
        print(result[i],end=', ')


    
