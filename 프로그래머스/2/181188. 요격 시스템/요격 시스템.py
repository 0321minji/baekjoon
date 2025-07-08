def solution(targets):
    answer = 0
    temp=[]
    targets.sort(key=lambda x: x[1])
    l=len(targets)
    tmp=targets[0][1]-1
    
    for i in range(l-1):
        # print(tmp,answer,targets[i],targets[i+1])
        if tmp>=targets[i+1][0]:
            continue
        else:
            answer+=1
            tmp = targets[i+1][1]-1

    
    return answer+1