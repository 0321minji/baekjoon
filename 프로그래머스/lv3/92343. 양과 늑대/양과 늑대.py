import sys
input=sys.stdin.readline

def getNextNode(i,prev,adj_list):
    nextNode=[a for a in prev if a!=i]
    #이전에 방문했던 노드들 중 자기가 아닌 것들 리스트화
    for j in range(len(adj_list)):
        if adj_list[i][j]:
            nextNode.append(j)
    return nextNode

def dfs(i,sheep,wolf,prev,adj_list,info):
    global answer
    nextNode=getNextNode(i,prev,adj_list)

    if sheep<=wolf or not nextNode:
        if answer<sheep:
            answer=sheep
        return

    for node in nextNode:
        if info[node]: #늑대가 있는 경우
            dfs(node,sheep,wolf+1,nextNode,adj_list,info)
        else:
            dfs(node,sheep+1,wolf,nextNode,adj_list,info)
        

def solution(info,edges):
    global answer
    answer=1
    adj_list=[[0]*len(info) for _ in range(len(info))]
    #인접한 노드를 기록할 리스트
    for a,b in edges:
        adj_list[a][b]=1

    dfs(0,1,0,[0],adj_list,info)

    return answer
