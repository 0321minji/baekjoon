import sys, heapq
input=sys.stdin.readline

n,m,k=map(int,input().split())
beer=[list(map(int,input().split())) for _ in range(k)]
beer=sorted(beer,key=lambda x:x[1])

temp=0
pq=[]
result=-1

for i in beer:
    temp+=i[0]
    heapq.heappush(pq,i[0])

    if len(pq)==n:
        if temp>=m:
            result=i[1]
            break
        else:
            temp-=heapq.heappop(pq)
print(result)
