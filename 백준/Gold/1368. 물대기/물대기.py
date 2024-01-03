import sys, heapq
input=sys.stdin.readline

n=int(input())
w=[int(input()) for _ in range(n)]
p=[list(map(int,input().split())) for _ in range(n)]
node=[]
for i in range(n):
    heapq.heappush(node,(w[i],i))

result=0
visit=[0]*(n)

while node:
    pay,nd= heapq.heappop(node)
    if visit[nd]:
        continue
    visit[nd]=1
    result+=pay
    
    for nxt in range(n):
        if nxt!=nd and w[nxt]>p[nd][nxt]:
            w[nxt]=p[nd][nxt]
            heapq.heappush(node,(w[nxt],nxt))
print(result)
