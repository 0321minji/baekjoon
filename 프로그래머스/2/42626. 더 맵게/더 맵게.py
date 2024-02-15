import heapq

def solution(scoville, K):
    answer = 0
    sc=[]
    for i in scoville:
        heapq.heappush(sc,i)
    
    def mix(sc):
        cnt=0
        while len(sc)>=2:
            a=heapq.heappop(sc)
            if a>=K:
                return 0
            b=heapq.heappop(sc)
            heapq.heappush(sc,(a+b*2))
            cnt+=1
            temp=heapq.heappop(sc)
            #print(sc,temp,cnt)
            if temp>=K:
                return cnt
            heapq.heappush(sc,temp)
        return -1
    answer=mix(sc)
    return answer