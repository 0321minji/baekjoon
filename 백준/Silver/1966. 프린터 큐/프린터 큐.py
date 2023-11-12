import sys
input=sys.stdin.readline

case=int(input())

for i in range(case):
    m,n=map(int,input().split())
    ans=[0]*m; ans[n]=1
    test=[]
    test=list(map(int,input().split()))
    count=0
    
    while(1):
        if(test[0]==max(test)):
            del test[0]
            count+=1
            if(ans[0]==1):
                print(count)
                break
            else:
                del ans[0]
        else:
            test.append(test[0])
            del test[0]
            ans.append(ans[0])
            del ans[0]