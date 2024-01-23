def solution(genres, plays):
    answer = []
    
    dic1={}
    dic2={}
    
    for i,(g,p) in enumerate(zip(genres,plays)):
        if g not in dic1:
            dic1[g]=[(i,p)]
        else:
            dic1[g].append((i,p))
        if g not in dic2:
            dic2[g]=p
        else:
            dic2[g]+=p
    
    dic2=sorted(dic2.items(),key=lambda x:x[1], reverse=True)

    for k,v in dic2:
        temp=sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]
        for i,p in temp:
            answer.append(i)
    return answer