def solution(diffs, times, limit):
    answer = 0
    n=len(diffs)
    # 이분탐색
    dp=0
    
    def binary_search(level):
        time=0
        for i in range(n):
            t=times[i]
            diff=diffs[i]
            if level>=diff:
                time+=t
            else:
                cnt = diff-level
                time+=cnt*(t+times[i-1])+t
            if time>limit:
                return False
        return True
    
    left=1
    right=max(diffs)
    while left<=right:
        mid = (left+right)//2
        if binary_search(mid):
            answer=mid
            right=mid-1
        else:
            left=mid+1
    return answer