def solution(n, times):
    answer = 0
    times.sort()
    low=1; high=max(times)*n
    
    while low<=high:
        mid=(low+high)//2
        cnt=0
        
        for t in times:
            #t 시간을 가진 심사관이 mid 동안 심사한 사람의 수
            cnt+=mid//t
            if cnt>=n:
                break
                
        if cnt>=n:
            answer=mid
            high=mid-1
        elif cnt<n:
            low=mid+1
        
    return answer