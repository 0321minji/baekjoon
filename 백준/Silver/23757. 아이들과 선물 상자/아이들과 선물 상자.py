import sys, heapq
input=sys.stdin.readline

n,m=map(int,input().split())
c=list(map(int,input().split()))
w=list(map(int,input().split()))

pq=[]
for i in range(n):
    heapq.heappush(pq,-c[i])

result=1
for i in range(m):
    temp=heapq.heappop(pq)
    if w[i]>-temp:
        result=0
        break
    heapq.heappush(pq,-(-temp-w[i]))

print(result)
