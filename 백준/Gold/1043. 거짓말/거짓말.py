import sys
input=sys.stdin.readline
##union-find

def find(parent,x):
    if x!=parent[x]:
        parent[x]=find(parent,parent[x])
    return parent[x]

def union(parent,a,b,mem):
    ap=find(parent,a)
    bp=find(parent,b)

    #진실을 아는 사람이면 그냥 return
    if ap in mem and bp in mem:
        return
    
    #a/b둘 중 한명이 진실을 아는 사람이면 하나로 묶
    if ap in mem:
        parent[bp]=ap
    elif bp in mem:
        parent[ap]=bp
        
    #둘 다 모르면 크기 비교후 묶
    else:
        if ap<bp:
            parent[bp]=ap
        else:
            parent[ap]=bp


n,m=map(int,input().split())
truth=list(map(int,input().split()))[1:]

g=[]
parent=list(range(n+1))

for i in range(m):
    temp=list(map(int,input().split()))
    people=temp[1:]

    for j in range(temp[0]-1):
        union(parent,people[j],people[j+1],truth)
    g.append(temp[1:])

result=0

for i in g:
    for j in range(len(i)):
        if find(parent,i[j]) in truth:
            break
            ## 부모가 진실을 알고 있으면 break
    else:
         result+=1
print(result)
    
