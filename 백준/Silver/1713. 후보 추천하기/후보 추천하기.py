import sys
input=sys.stdin.readline

def check(i):
    for j in temp:
        if j[2]==i:
            j[0]+=1
            return True
    return False
n=int(input())
total=int(input())
who=list(map(int,input().split()))
temp=[]

for i in range(total):
    state=check(who[i])
    #print(state)
    #이미 게시되었는지 확인
    if state:
        continue
    #사진틀이 비어있는 경우 -> 바로 추가 (추천수,게시시간,후보번호)
    if len(temp)<n:
        temp.append([1,i,who[i]])
    #삭제해야하는 경우 -> 정렬(추천수, 게시시간 기준으로 정렬됨 -> 0번째 pop)
    else:
        temp.sort()
        temp.pop(0)
        temp.append([1,i,who[i]])
    #print(temp)
result=[i[2] for i in temp]
result.sort()
print(*result)
