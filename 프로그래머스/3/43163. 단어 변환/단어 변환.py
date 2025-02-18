def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    
    if begin in words:
        words.remove(begin)

    answer=bfs(begin,target,words)
    if answer:
        return answer
    return 0

def bfs(begin,target,words):
    que=[(begin,0,words)]
    length=len(target)
    res=[begin]

    while que:
        now,cnt,words=que.pop(0)
        temp=words[:]
        if now==target:
            return cnt
        
        for i in range(length):
            for word in words:
                if now[:i]+now[i+1:] == word[:i]+word[i+1:]:
                    #words.remove(word)
                    temp.remove(word)
                    que.append((word,cnt+1,temp))


# ## dfs 
# def dfs(depth,now,target,words,res):
#     global ans
#     length=len(now)
#     if now ==target:
#         ans=min(ans,depth)
#         return
    
#     for i in range(length):
#         for word in words:
#             if now[:i]+now[i+1:] == word[:i]+word[i+1:] and now not in res:
#                 # print(now, word)
#                 res.append(now)
#                 words.remove(word)
#                 dfs(depth+1,word,target,words,res)
#                 words.append(word)
#                 res.remove(now)
#     return ans
