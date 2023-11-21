import sys, heapq
input=sys.stdin.readline

def dijk(start, n):
    global load, result
    hq=[]
    for i in range(1,n+1):
        if i==start:
            continue
        heapq.heappush(hq,(load[start][i],i))

    while hq:
        dist, node= heapq.heappop(hq)
        if load[start][node]<dist:
            continue
        for nei in range(1,n+1):
            if node==nei or start == nei:
                #자기 자신
                continue
            if dist+ load[node][nei] < load[start][nei]:
                load[start][nei]= dist+load[node][nei]
                heapq.heappush(hq, (dist+load[node][nei], nei))
                result[start][nei]=result[start][node]
    
            

inf=10**8
n,m=map(int,input().split())
load=[[inf]*(n+1) for _ in range(n+1)]
result=[['-']*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,t=map(int,input().split())
    load[a][b]=load[b][a]=t
    result[a][b]=b
    result[b][a]=a

for i in range(1,n+1):
    dijk(i,n)

for res in result[1:]:
    print(*res[1:])
    
   