from itertools import combinations
from collections import defaultdict

def solution(line):
    answer = []
    stars = defaultdict(list)
    maxX = float('-inf')
    minX = float('inf')

    #교점 찾기
    for combi in combinations(line,2):
        a,b,e=combi[0]
        c,d,f=combi[1]
        
        #분모
        denominator = a*d-b*c
        if denominator == 0:
            continue
        
        #분자
        numeratorX = b*f-e*d
        numeratorY = e*c-a*f
        
        x=numeratorX/denominator
        y=numeratorY/denominator
        if x==int(x) and y==int(y):
            y=int(y)
            x=int(x)
            stars[y].append(x)
            maxX=max(x,maxX)
            minX=min(x,minX)
    
    #print(stars,maxX,minX)
    keys=stars.keys()

    #출력
    for i in range(max(keys),min(keys)-1,-1):
        tmp=""
        for j in range(minX,maxX+1):
            if j in stars[i]:
                tmp+="*"
            else:
                tmp+="."
        answer.append(tmp)
    return answer