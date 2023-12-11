import sys
input=sys.stdin.readline

def solve():
    #0-추천수 1-시간
    photo=[[10**3,10**3] for _ in range(101)]
    stu=[]
    for i in range(t):
        if g[i] in stu:
            photo[g[i]][0]+=1
        elif len(stu)<n:
            photo[g[i]]=[1,i]
            stu.append(g[i])
        else:
            #추천 젤 작은거&젤 오래된거 삭제 
            index=photo.index(min(photo,key=lambda x:(x[0],x[1])))
            #print(index,photo)
            photo[index]=[10**3,10**3]
            stu.remove(index)
            photo[g[i]]=[1,i]
            stu.append(g[i])
    stu.sort()
    print(*stu)
            
            
n=int(input())
t=int(input())
g=list(map(int,input().split()))
solve()
