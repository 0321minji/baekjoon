from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    br=deque([0]*bridge_length)
    tr=deque(truck_weights)
    SUM=0

    while tr:
        SUM-=br.popleft()
        temp=0
        if SUM+tr[0]<=weight:
            temp=tr.popleft()
        SUM+=temp
        br.append(temp)
        answer+=1
    answer+=bridge_length
    return answer