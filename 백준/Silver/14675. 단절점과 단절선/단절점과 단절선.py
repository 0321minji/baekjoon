import sys
input=sys.stdin.readline

n=int(input())
tree=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

q=int(input())
for _ in range(q):
    t,k=map(int,input().split())
    #리프노드&자식이 1개 뿐인 부모 =>no
    if t==1:
        if len(tree[k])<=1:
            print('no')
            continue
    print('yes')
