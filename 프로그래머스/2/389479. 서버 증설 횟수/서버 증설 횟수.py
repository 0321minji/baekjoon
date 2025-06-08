from collections import deque

def solution(players, m, k):
    answer = 0
    server =[0]*k
    server = deque(server)
    
    
    for i in range(24):
        #앞에꺼 빼기
        server.popleft()
        print(i,sum(server))
        
        #이용자 수 비교 후 증설 여부 결정
        now = sum(server)
        if (now+1)*m<=players[i]:
            print('here')
            # 몇 개 추가?
            temp=players[i]//m-now
            server.append(temp)
            answer+=temp
        else:
            server.append(0)
        
        
    return answer