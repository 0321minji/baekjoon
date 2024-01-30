from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    br=deque([0]*(bridge_length))
    tr=deque(truck_weights)
    #print(br)
    SUM=0
    while tr:
        answer+=1
        SUM-=br.popleft()
        temp=0
        if SUM+tr[0]<=weight:
            temp=tr.popleft()
        br.append(temp)
        SUM+=temp
        #print(br)
    answer+=bridge_length
    return answer

            
    return answer