import sys, heapq
input=sys.stdin.readline

n=int(input())
time=[list(map(int,input().split())) for _ in range(n)]
time.sort()

que=[]
heapq.heappush(que,time[0][1])

for i in range(1,n):
    #끝나는 시간 넣기
    #끝나는 시간이 더 늦으면 강의실 추가
    if que[0]> time[i][0]:
        heapq.heappush(que,time[i][1])
    #아니라면 수업 교체(끝나는 시간 갱신)
    else:
        heapq.heappop(que)
        heapq.heappush(que,time[i][1])
print(len(que))
