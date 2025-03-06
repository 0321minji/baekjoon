import sys
input=sys.stdin.readline
import heapq

n,m=map(int,input().split())
graph = [ [] for _ in range(n+1)]



for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])


result=[10**9]*(n+1)
result[1]=0

def solve(start):
    que=[]
    heapq.heappush(que,[result[start],start])
    while que:
        dist,now= heapq.heappop(que)
        if dist > result[now]:
            continue
        
        for i in graph[now]:
            temp = dist+i[1]
            nxt = i[0]
            if temp<result[nxt]:
                result[nxt]=temp
                heapq.heappush(que,[result[nxt],nxt])
    return result

print(solve(1)[-1])