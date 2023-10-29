def dfs(num):
    global cnt
    if len(n) == 1:
        cnt +=1
        return
    L = set(list(num))
    if len(L) == 1:
        cnt+=1
        return
    else:
        dfs(num[1:])
        dfs(num[:-1])

n = input()
cnt = 0
dfs(n)
print(cnt)
