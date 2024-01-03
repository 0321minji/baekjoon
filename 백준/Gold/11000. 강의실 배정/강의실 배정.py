import sys
input=sys.stdin.readline
import heapq

n=int(input())

time=[]

for i in range(n):
    inn=list(map(int,input().split()))
    time.append(inn)
    
time.sort(key=lambda x:(x[0],x[1]))

que=[]
heapq.heappush(que,time[0][1])

for i in range(1,n):
    if que[0] > time[i][0]:
        heapq.heappush(que,time[i][1])
    else:
        heapq.heappop(que)
        heapq.heappush(que,time[i][1])

print(len(que))
