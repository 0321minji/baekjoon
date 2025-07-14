from itertools import combinations

def solution(n, q, ans):
    answer = 0
    num=list(i+1 for i in range(n))
    m=len(ans)
    
    for i in combinations(num,5):
        for j in range(m):
            if len(set(i)&(set(q[j]))) != ans[j]:
                break
        else:
            answer+=1        
    
    return answer