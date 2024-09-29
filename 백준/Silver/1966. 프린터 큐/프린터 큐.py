import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    important=list(map(int,input().split()))
    num=important[m]
    arr=[]
    for i in range(n):
        arr.append([important[i],i])
    cnt=0
    while True:
        # 맨 앞에 있는게 우선순위가 가장 크면
        if arr[0][0]==max(important):
            cnt+=1
            if arr[0][1]==m:
                print(cnt)
                break
            important.remove(arr[0][0])
            arr.remove(arr[0])
        # 그게 아니면 뒤로 추가
        else:
            arr.append(arr[0])
            arr.remove(arr[0])

        #print(arr,important)
