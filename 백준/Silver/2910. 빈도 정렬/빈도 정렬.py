import sys
input=sys.stdin.readline

n,c=map(int,input().split())
m=list(map(int,input().split()))
count={}
index=1

for t in m:
    if t in count:
        count[t][0]+=1
    else:
        count[t]=[1,index]
        index+=1

result=[[a,b] for a,b in count.items()]
result.sort(key=lambda x:(-x[1][0],x[1][1]))
res=[]

for i,j in result:
    res+=[i]*j[0]
    
print(*res)
