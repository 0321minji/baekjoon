from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre=defaultdict(int)
    music=defaultdict(list)
    for g,p in zip(enumerate(genres),plays):
        genre[g[1]]+=p
        music[g[1]].append([g[0],p])
    
    # for key, items in lis
    for key, value in sorted(list(genre.items()), key=lambda x:-x[1]):
        cnt=0
        for index, _ in sorted(music[key],key=lambda x:-x[1]):
            if cnt==2:
                break
            answer.append(index)
            cnt+=1

    return answer