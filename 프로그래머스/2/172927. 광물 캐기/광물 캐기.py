from itertools import permutations 
answer = 0

def solution(picks, minerals):
    global answer
    
    pick=[]
    use=[[1,1,1],[5,1,1],[25,5,1]]
    # stone={"diamond":25,"iron":5,"stone":1}
    
    for index, num in enumerate(picks):
        tmp=[index]*num
        pick.extend(tmp)
        
    n=sum(picks)    
    m=len(minerals)
    #m//5 개 만큼 쓸 수 이씅
    cnt=min((m+4)//5,n)
    
    chunk=[]
    for i in range(cnt):
        s=r=d=0
        start=i*5
        for j in range(5):
            index=start+j
            if index<m:
                tmp=minerals[index]
                if tmp=='diamond':
                    d+=1
                elif tmp=='iron':
                    r+=1
                else:
                    s+=1
            else:
                break        
        chunk.append((d,r,s))
    
    chunk.sort(key=lambda x:(-x[0],-x[1],-x[2]))
    # 캐기 어려운 광물이 많은 순으로 정렬
    
    pick.sort()
    #print(pick)
    #print(cnt,chunk)
    
    for i in range(cnt):
        now=pick[i]
        for j in range(3):
            #print(now,use[now][j],chunk[i][j])
            answer+=(use[now][j]*chunk[i][j])
    
    return answer