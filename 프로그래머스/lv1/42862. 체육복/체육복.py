def solution(n, lost, reserve):
    answer = 0
    #가지고 온 사람이 도난당한 경우 제거
    reserved=set(reserve)-set(lost)
    losted=set(lost)-set(reserve)
    
    for i in sorted(reserved):
        if i-1 in losted:
            losted-={i-1}
            continue
        if i+1 in losted:
            losted-={i+1}

    answer=n-len(losted)

    return answer