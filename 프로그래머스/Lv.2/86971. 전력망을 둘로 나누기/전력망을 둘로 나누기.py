def makeTree(c):
    global parent, tree
    for node in connect[c]:
        if node != parent[c]:
            tree[c].append(node)
            parent[node]=c
            makeTree(node)

def countNode(c):
    for node in tree[c]:
        countNode(node)
        size[c]+=size[node]

def solution(n, wires):
    global connect, parent,tree,size
    parent=[-1]*(n+1)
    size=[1]*(n+1)
    connect=[[] for _ in range(n+1)]
    tree=[[] for _ in range(n+1)]
    answer = 100
    for a,b in wires:
        connect[a].append(b)
        connect[b].append(a)
    makeTree(1)
    countNode(1)
    for i in range(1,n+1):
        temp=abs((n-size[i])-size[i])
        answer=min(answer,temp)
    return answer

