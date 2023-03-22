import sys
input=sys.stdin.readline

def change(string):
    st=0;ed=0
    count=0
    for i in range(len(string)):
        if string[i]=='}':
            ed+=1
            if ed>st:
                ed-=1; st+=1; count+=1
        elif string[i]=='{':
            st+=1
    if st!=ed:
        temp=abs(st-ed)
        count+=temp//2


    return count

k=0
    
while(1):
    k+=1
    string=input().rstrip()

    if '-' in string:
        break
    result=change(string)
    print("%d. %d"%(k,result))