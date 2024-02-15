def bfs(start,dic,graph):
    queue=[start]
    visited={start:True}
    while queue:
        node=queue.pop(0)
        dic[node][node]=True
        if node not in graph:
            continue
        for i in graph[node]:
            if i not in visited:
                visited[i]=True
                for j in dic[node]: # 인접노드에 진/이긴 정보를 전달하는 과정
                    dic[i][j]=True 
                queue.append(i)


def solution(n, results): 
    dic=dict()  #각 노드에서 자기를 포함해서 자기가 진 노드를 담는 딕셔너리
    dic2=dict() #각 노드에서 자기를 포함해서 자기가 이긴 노드를 담는 딕셔너리
    graph={} #인접 정보를 담는 딕셔너리 (이긴 노드에서 진노드로)
    graph2={} # 인접 정보를 담는 딕셔너리 (진노드에서 이긴 노드로)
    for i in results: #초기화 
        x=i[0]
        y=i[1]
        if x not in graph:
            graph[x]=[y] 
        else:
            graph[x].append(y)
        if y not in graph2:
            graph2[y]=[x]
        else:
            graph2[y].append(x)
    for i in range(1,n+1): #초기화
        dic[i]={}
        dic2[i]={}


    for i in range(1,n+1): #모든 노드에 대해 bfs로 인접노드에게 진 정보를 전달
        bfs(i,dic,graph)
    for i in range(1,n+1): # 모든 노드에 대해 bfs로 인접노드에게 이긴 정보를 전달
        bfs(i,dic2,graph2)
    count=0 #정답을 저정하는 변수 
    for i in dic:
         if len(dic2[i])-1+len(dic[i]) == n: #자신을 포함해서 자기가 진노드와 이긴 노드의 합이 N이여야 순위가 정해진 것임 
            count+=1
    return count