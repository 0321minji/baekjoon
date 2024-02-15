import heapq
def solution(scoville, K):
    answer = 0
    sc=[]
    for i in scoville:
        heapq.heappush(sc,i)
    
    while len(sc)>=2:
        a=heapq.heappop(sc)
        if a>=K:
            return 0

        b=heapq.heappop(sc)
        if b==0:
            return -1
        heapq.heappush(sc,a+b*2)
        answer+=1
        temp=heapq.heappop(sc)
        if temp>=K:
            return answer
        heapq.heappush(sc,temp)
        
    return -1