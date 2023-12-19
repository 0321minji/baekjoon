import sys
input=sys.stdin.readline
#빼면서 풀기
def dfs(num):
    global cnt
    #길이가 1이면 하나만 더 빼면 되니까 cnt+1
    if len(n)==1:
        cnt+=1
        return
    L=set(list(num))
    #set 만들어서 만약 set 길이가 1이면 어떻게 빼던 같으니까 한가지 방법이니까 cnt+1 해주고 return함
    if len(L)==1:
        cnt+=1
        return
    else:
        #1 아니면 계속 탐색 해줘야하니까 왼에서 하나 뺀 경우 / 오에서 하나 뺀 경우 각각 재귀호출
        dfs(num[1:])
        dfs(num[:-1])
        
    
n=input().rstrip()
cnt=0
dfs(n)
print(cnt)
