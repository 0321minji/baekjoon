import sys
input=sys.stdin.readline

n=int(input())
word=[]
answer=0
for i in range(n):
    if i==0:
        goal=list(input().strip())
        goal.sort()
    else:
        temp=list(input().strip())
        temp.sort()
        if goal==temp:
            #print(temp)
            answer+=1
        else:
            word.append(temp)

for i in range(len(word)):
    if abs(len(goal)-len(word[i]))>1:
        continue
    w=goal[:]
    temp=word[i][:]
    j=0
    while(j<len(temp)):
        #print(temp,w,j)
        k=temp[j]
        if k in w:
            temp.remove(k)
            w.remove(k)
        else:
            j+=1
    #print(temp,w)
    if max(len(temp),len(w))<2:
        
        #print(word[i])
        answer+=1
            


print(answer)
