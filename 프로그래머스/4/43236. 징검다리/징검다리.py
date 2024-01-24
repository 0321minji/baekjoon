def solution(distance, rocks, n):
    answer = 0
    
    def bs(left,right):
        while left<=right:
            mid=(left+right)//2
            delete=0
            prev=0
            
            for r in rocks:
                d=r-prev
                if d<mid:
                    delete+=1
                    if delete>n:
                        break
                else:
                    prev=r
            if delete>n:
                right=mid-1
            else:
                answer=mid
                left=mid+1
        return answer
    
    left=1; right=distance
    rocks.sort()
    rocks.append(distance)
    return bs(left,distance)
    #return answer