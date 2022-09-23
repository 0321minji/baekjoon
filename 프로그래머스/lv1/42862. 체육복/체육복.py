def solution(n, lost, reserve):
    answer = 0
    clothes=[1]*(n+2)
    #2만큼 여유를 둬서 예외 상황 처리하기
    for i in lost:
        clothes[i]-=1
    for i in reserve:
        clothes[i]+=1
    for i in range(n+1):
        if clothes[i]==0 and clothes[i-1]>1:
            clothes[i]+=1; clothes[i-1]-=1
            continue
        if clothes[i]==0 and clothes[i+1]>1:
            clothes[i]+=1; clothes[i+1]-=1
    print(clothes)
    for i in range(1,n+1):
        if clothes[i]>=1:
            answer+=1
    return answer