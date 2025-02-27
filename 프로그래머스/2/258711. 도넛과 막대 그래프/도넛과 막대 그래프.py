# import sys
# sys.setrecursionlimit(10**6)
# def solution(edges):
#     n=len(edges)
#     graph={}
#     edgeIn=[]
#     for i in range(1,n+1):
#         graph[i]=[]
        
#     def init():
#         for a,b in edges:
#             if a not in graph:
#                 graph[a]=[]
#             graph[a].append(b)
#             edgeIn.append(b)
#     init()
#     # print(graph)
    
#     def findV():
#         for i in graph:
#             temp=len(graph[i])
#             if temp>2:
#                 return i
#             if temp==2 and i not in edgeIn:
#                 return i

#     v=findV()
#     if(len(edges))==10**6:
#         return [v,0,10**6,0]
#     print(max(edges))
#     def dfs(depth, now, visit):
#         if depth==len(edges):
#             return
#         if len(graph[now])==2:
#             return "eight"
#         if now in visit :
#             return "donut"
            
#         if len(graph[now])==0:
#             return "stick"
        
#         visit.append(now)
        
#         for nxt in graph[now]:
#             return dfs(depth+1,nxt,visit)
    
#     count=len(graph[v])
#     st=0
#     do=0
#     ei=0
#     for i in graph[v]:
#         res = dfs(0,i,[])
#         if res == 'stick':
#             st+=1    
#         elif res == 'donut':
#             do+=1
#         else:
#             ei+=1
#         if st+do+ei==count:
#             return [v,do,st,ei]
        
#     return answer
import sys
sys.setrecursionlimit(10**6)

def solution(edges):
    # n=len(edges)
    # graph={}
    cnt={}
    
        
    def init():
        for a,b in edges:
            if a not in cnt:
                cnt[a]=[0,0]
            if b not in cnt:
                cnt[b]=[0,0]
            cnt[a][0]+=1
            cnt[b][1]+=1
            
    init()
    # print(graph,cnt,max(cnt.values())[0])
    
    v=st=do=ei=0
    for i in cnt: 
        # print(cnt[i][1],cnt[i][0])
        if cnt[i][0]>2:
            v=i
            continue
        #2개 out
        if cnt[i][0]==2:
            if cnt[i][1]>0:
                ei+=1
            else:
                v=i
                continue
        if cnt[i][0]==0:
            st+=1
            
    do=cnt[v][0]-st-ei
    return [v,do,st,ei]
